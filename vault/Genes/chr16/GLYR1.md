---
symbol: "GLYR1"
type: "gene"
col: 6439
ensembl_id: "ENSG00000140632"
name: "glyoxylate reductase 1 homolog"
location: "16p13.3"
module: 52
arm: "+"
pooled_cpm: 99.32
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# GLYR1

*glyoxylate reductase 1 homolog* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.06× (z +21.9, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.788× (z -9.7, q 2e-19, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.344×, SNU-1 0.310×, H4 0.340×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 3 lines (AsPC-1 0.579×, Hs 766T 0.572×, HOP62 0.613×; ⚠ cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.130×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SW 1271 0.0933×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS53]] (+0.58, fdr 1e-05), [[LIN52]] (+0.58, fdr 1e-05), [[SPG7]] (+0.58, fdr 1e-05); moves opposite to [[RYBP]] (-0.57, fdr 2e-05), [[GNA13]] (-0.56, fdr 1e-05), [[SPOPL]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6439.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.06×** | +21.9 | 0e+00 | 45/48 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +18.4 | 0e+00 | 42/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +16.9 | 0e+00 | 41/49 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +16.5 | 0e+00 | 43/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +15.2 | 0e+00 | 43/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.58×** | +13.9 | 1e-41 | 43/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +13.7 | 9e-41 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.55×** | +13.2 | 5e-38 | 42/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +13.2 | 9e-38 | 41/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +12.1 | 8e-32 | 46/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.48×** | +11.8 | 1e-30 | 38/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +11.3 | 1e-27 | 40/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.44×** | +10.6 | 9e-25 | 38/48 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +10.2 | 6e-23 | 36/50 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +9.4 | 2e-19 | 35/48 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +8.8 | 6e-17 | 36/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +8.4 | 1e-15 | 24/48 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.67×** | +8.2 | 1e-14 | 36/49 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +8.1 | 1e-14 | 30/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +7.8 | 2e-13 | 26/48 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.34×** | +6.3 | 8e-09 | 29/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6439.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.344×, SNU-1 0.310×, H4 0.340×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 3 lines (AsPC-1 0.579×, Hs 766T 0.572×, HOP62 0.613×; ⚠ cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.130×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SW 1271 0.0933×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.788×** | -9.7 | 2e-19 | 31/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.812×** | -6.3 | 8e-08 | 27/49 (SHP-77, SW480, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.838× | -5.3 | 2e-05 | 23/48 (AsPC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.860× | -4.6 | 7e-04 | 21/49 (HEC-1-A, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.904× | -4.2 | 0.003 | 7/48 (SW1417, SW 1088, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.886× | -3.5 | 0.035 | 14/48 (NCI-H1573, A498, …) | top dose only |  |
| [[Imiquimod (maleate) (drug)]] 0.05 µM |  | 0.882× | -3.5 | 0.035 | 11/47 (SK-MEL-2, KATO III, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.899× | -3.2 | 0.087 | 9/48 (CHP-212, NCI-H2347, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.902× | -3.1 | 0.11 | 3/47 (A-427, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.906× | -3.0 | 0.15 | 3/47 (CFPAC-1, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6439. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 84.0 | 14 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +25.6) | — |
| [[SW480 (line)]] | alt | 105 | 12 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +16.5) | — |
| [[PANC-1 (line)]] | alt | 115 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +19.1) | — |
| [[COLO 205 (line)]] | alt | 103 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.89× (z +16.8) | — |
| [[HEC-1-A (line)]] | alt | 110 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +17.2) | — |
| [[LoVo (line)]] | wt | 88.4 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.92× (z +19.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 74.5 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.32× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.05× (z +9.0) | — |
| [[RKO (line)]] | wt | 105 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 109 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +10.2) | [[Selinexor (drug)]] 5 µM 0.572× (z -9.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[KATO III (line)]] | alt | 97.8 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +13.5) | — |
| [[NCI-H23 (line)]] | alt | 88.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 103 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.60× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 92.5 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.55× (z +15.5) | — |
| [[SNU-1 (line)]] | wt | 102 | 3 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.30× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 73.9 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 127 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +11.1) | [[Selinexor (drug)]] 5 µM 0.579× (z -10.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 68.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 105 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 74.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +9.8) | [[Selinexor (drug)]] 5 µM 0.613× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW1417 (line)]] | alt | 112 | 3 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.58× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 111 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 96.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 139 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.496× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 55.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 102 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -26.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 110 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.8) | — |
| [[A-172 (line)]] | wt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.5) | — |
| [[A-427 (line)]] | wt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.03× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 92.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.27× (z +8.7) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 86.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +8.6) | — |
| [[H4 (line)]] | wt | 97.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 84.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.3) | — |
| [[J82 (line)]] | alt | 114 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 74.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 99.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 89.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.99× (z +8.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW 1271 (line)]] | alt | 88.9 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0933× (z -10.9) |
| [[A498 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 94.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 78.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 97.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 87.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6439), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS53]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[LIN52]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SPG7]] | +0.58 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CDK11B]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SENP5]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ACO2]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[NPLOC4]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[PITPNA]] | +0.55 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[CDK11A]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[GOLGA3]] | +0.54 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[ALG11]] | +0.54 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[XPNPEP3]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RYBP]] | -0.57 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[GNA13]] | -0.56 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[SPOPL]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[C12orf29]] | -0.54 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[HMGN4]] | -0.54 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[PPP2R2A]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[PRKAA1]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PRTG]] | -0.52 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[NGFR]] | -0.51 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[CAPZA2]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[IFTAP]] | -0.50 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[DMXL1]] | -0.50 | -0.37 / -0.52 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GLYR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PRTG]] | B | PRTG activity lowers GLYR1's level | lines that do not express PRTG (14) vs lines expressing it (36) | 1.16× higher at baseline in the lines without PRTG | 0.089 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-15.7, -0.7); signed map (-47.3, -0.5). **Vector** length 91.2, 25.9% of its response variance represented; |z| ≥ 3 in 1,379 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.7 | +10.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.2 | +10.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.9 | +12.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +16.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +11.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +8.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +6.3 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +1.6 | -0.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -11.5 | -9.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -5.5 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -5.2 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | +0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | glyoxylate reductase 1 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,803,203-4,847,288 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BM045, HIBDL, NP60, N-PAC |
| Gene groups (HGNC) | PWWP domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q49A26](https://www.uniprot.org/uniprotkb/Q49A26) (Cytokine-like nuclear factor N-PAC):

> Cytokine-like nuclear factor with chromatin gene reader activity involved in chromatin modification and regulation of gene expression. Acts as a nucleosome-destabilizing factor that is recruited to genes during transcriptional activation. Recognizes and binds histone H3 without a preference for specific epigenetic markers and also binds DNA. Interacts with KDM1B and promotes its histone demethylase activity by facilitating the capture of H3 tails, they form a multifunctional enzyme complex that …

**Summary**, from NCBI Gene [84656](https://www.ncbi.nlm.nih.gov/gene/84656):

> Enables several functions, including chromatin-protein adaptor activity; histone binding activity; and nucleosome binding activity. Involved in transcription elongation-coupled chromatin remodeling and transcription initiation-coupled chromatin remodeling. Located in nucleoplasm. Part of nucleosome. Is active in chromatin. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24434) · Entrez [84656](https://www.ncbi.nlm.nih.gov/gene/84656) · UniProt [Q49A26](https://www.uniprot.org/uniprotkb/Q49A26) · Ensembl [ENSG00000140632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140632)

## Data

Gene col 6439: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6439); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6439, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6439]; `tensor/DDL_lfc|DDL_z.npy` [6439]; `embed/gene_vectors.npy` [6439]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6439 or target_col == 6439). Every well: [[GLYR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLYR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
