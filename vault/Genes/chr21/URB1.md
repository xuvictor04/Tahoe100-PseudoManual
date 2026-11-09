---
symbol: "URB1"
type: "gene"
col: 6607
ensembl_id: "ENSG00000142207"
name: "URB1 ribosome biogenesis factor"
location: "21q22.11"
module: 18
arm: "+"
pooled_cpm: 57.96
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 14
n_dd_up_clean: 19
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# URB1

*URB1 ribosome biogenesis factor* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (21 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.73× (z +16.8, q 0e+00, up in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.71× (z +8.7, q 4e-16, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.780× (z -5.9, q 2e-06, down in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.711× (z -5.5, q 1e-05, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDN1]] (+0.81, fdr 7e-06), [[NSUN2]] (+0.80, fdr 7e-06), [[WDR4]] (+0.77, fdr 7e-06); moves opposite to [[TCEAL3]] (-0.66, fdr 7e-06), [[KMT2A]] (-0.66, fdr 7e-06), [[ZMYM5]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 26 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6607.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.73×** | +16.8 | 0e+00 | 48/48 (MIA PaCa-2, NCI-H2347, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.72×** | +16.7 | 0e+00 | 46/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.40×** | +14.6 | 0e+00 | 44/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.26×** | +13.6 | 3e-40 | 42/48 (A-172, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.71×** | +8.7 | 4e-16 | 41/48 (A-172, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.32×** | +7.3 | 2e-11 | 30/35 (HOP62, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +6.8 | 8e-10 | 31/49 (A498, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +6.5 | 6e-09 | 33/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[EX229 (drug)]] 5 µM |  | **2.05×** | +6.3 | 2e-08 | 36/48 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.45×** | +6.2 | 4e-08 | 27/48 (PANC-1, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +6.1 | 5e-08 | 30/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change; position correction uncertain | **1.46×** | +6.0 | 8e-08 | 25/43 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.46×** | +6.0 | 8e-08 | 25/49 (HS-578T, Panc 03.27, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.99×** | +6.0 | 8e-08 | 36/48 (MIA PaCa-2, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM | ⚠ position correction uncertain | **1.98×** | +6.0 | 1e-07 | 36/48 (MIA PaCa-2, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +5.9 | 1e-07 | 26/48 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.59×** | +5.5 | 1e-06 | 31/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.87×** | +5.4 | 2e-06 | 29/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.74×** | +4.8 | 3e-05 | 26/48 (MIA PaCa-2, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.42×** | +4.2 | 6e-04 | 19/48 (A498, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.1 | 8e-04 | 21/48 (CFPAC-1, A-172, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.004 | 16/49 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.006 | 22/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.007 | 21/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6607.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.780×** | -5.9 | 2e-06 | 25/48 (NCI-H460, SW1417, …) | top dose only | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.711×** | -5.5 | 1e-05 | 27/47 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.784×** | -4.8 | 3e-04 | 25/48 (NCI-H460, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.754×** | -4.6 | 7e-04 | 22/47 (NCI-H2030, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.775×** | -4.3 | 0.002 | 20/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.767×** | -4.3 | 0.002 | 23/48 (SNU-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.776×** | -4.3 | 0.002 | 21/47 (LS 180, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.783×** | -4.1 | 0.003 | 23/49 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.782×** | -4.0 | 0.004 | 23/47 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.792×** | -3.9 | 0.005 | 22/47 (A-427, HCT15, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.826×** | -3.6 | 0.016 | 16/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.809×** | -3.6 | 0.016 | 22/48 (LoVo, A-427, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.827×** | -3.4 | 0.035 | 18/49 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.848× | -3.3 | 0.037 | 15/49 (NCI-H460, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.822×** | -3.3 | 0.037 | 14/48 (KATO III, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6607. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 26.8 | 9 (9 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 6.51× (z +11.6) ⚠ unreliable plate only | — |
| [[HOP62 (line)]] | alt | 47.2 | 6 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.00× (z +13.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1573 (line)]] | alt | 51.6 | 6 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.32× (z +12.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 82.3 | 1 (1 ⚠) | 5 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.70× (z +10.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -15.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.376× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 24.5 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.52× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 57.0 | 4 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.17× (z +10.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.03× (z +9.3) | [[Ixazomib citrate (drug)]] 0.5 µM 0.402× (z -8.5) |
| [[A-172 (line)]] | wt | 34.3 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.18× (z +14.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 8.23× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 34.4 | 4 (4 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.95× (z +10.7) ⚠ unreliable plate only | — |
| [[C32 (line)]] | wt | 32.1 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.67× (z +10.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HS-578T (line)]] | alt | 40.6 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.43× (z +11.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2347 (line)]] | alt | 31.8 | 4 (4 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.95× (z +12.1) ⚠ unreliable plate only | — |
| [[SW480 (line)]] | alt | 83.8 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +11.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 71.7 | 3 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 6.00× (z +14.3) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 65.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.10× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change; position correction uncertain | — |
| [[SNU-423 (line)]] | alt | 20.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.26× (z +10.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[COLO 205 (line)]] | alt | 21.9 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 5.61× (z +8.6) ⚠ cell-cycle shift, explains ~34% of this change | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.138× (z -9.1) |
| [[Hs 766T (line)]] | wt | 39.0 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.46× (z +10.3) ⚠ unreliable plate only | — |
| [[HT-29 (line)]] | alt | 22.9 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.22× (z +9.3) ⚠ unreliable plate only | — |
| [[Panc 03.27 (line)]] | alt | 33.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.59× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 67.4 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.301× (z -12.1) |
| [[SW1417 (line)]] | alt | 83.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.87× (z +10.1) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -14.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW48 (line)]] | wt | 89.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.313× (z -8.7) |
| [[A-427 (line)]] | wt | 55.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.336× (z -9.4) |
| [[A498 (line)]] | wt | 121 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.31× (z +10.4) ⚠ unreliable plate only | — |
| [[C-33 A (line)]] | alt | 73.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change; position correction uncertain |
| [[LOX-IMVI (line)]] | wt | 55.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.57× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 51.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.84× (z +8.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2030 (line)]] | alt | 96.8 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.67× (z +8.6) ⚠ unreliable plate only | — |
| [[NCI-H661 (line)]] | alt | 47.5 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0926× (z -8.8) |
| [[PANC-1 (line)]] | alt | 76.0 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.30× (z +8.9) ⚠ unreliable plate only | — |
| [[RKO (line)]] | wt | 92.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change; position correction uncertain |
| [[SHP-77 (line)]] | alt | 85.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.62× (z +9.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 89.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 37.2 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.25× (z +9.1) ⚠ unreliable plate only | — |
| [[A549 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 71.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6607), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDN1]] | +0.81 | +0.81 / +0.80 | both halves | 7e-06 | STRING 443 |
| [[NSUN2]] | +0.80 | +0.72 / +0.84 | both halves | 7e-06 |  |
| [[WDR4]] | +0.77 | +0.77 / +0.80 | both halves | 7e-06 | STRING 408 |
| [[EIF3B]] | +0.77 | +0.76 / +0.73 | both halves | 7e-06 | same gene group |
| [[MYBBP1A]] | +0.77 | +0.81 / +0.72 | both halves | 7e-06 | same gene group; STRING 696 |
| [[EARS2]] | +0.77 | +0.76 / +0.72 | both halves | 7e-06 | STRING 480 |
| [[PUM3]] | +0.76 | +0.75 / +0.76 | both halves | 7e-06 | STRING 688 |
| [[WDR3]] | +0.76 | +0.78 / +0.77 | both halves | 7e-06 | STRING 684 |
| [[DKC1]] | +0.76 | +0.81 / +0.70 | both halves | 7e-06 | same gene group; STRING 659 |
| [[POLR1A]] | +0.75 | +0.71 / +0.78 | both halves | 7e-06 | STRING 906 |
| [[TRAP1]] | +0.75 | +0.73 / +0.81 | both halves | 7e-06 |  |
| [[CHID1]] | +0.75 | +0.72 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEAL3]] | -0.66 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[KMT2A]] | -0.66 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.65 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[GIHCG]] | -0.64 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[PNRC1]] | -0.62 | -0.51 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises URB1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[DUXAP9]] | B | DUXAP9 activity raises URB1's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without DUXAP9 | 0.088 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-12.1, -37.1); signed map (-5.1, -50.6). **Vector** length 130, 42.2% of its response variance represented; |z| ≥ 3 in 1,464 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.64 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.7 | +16.8 |
|  | [[EX229 (drug)]] 5 µM |  | +5.8 | +6.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM | ⚠ position correction uncertain | +5.6 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +8.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.0 | +3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.9 | +6.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -12.1 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.8 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.7 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.1 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.1 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | URB1 ribosome biogenesis factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:32,311,018-32,393,012 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0539, NPA1; previously C21orf108 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Ribosome biogenesis factors; Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [O60287](https://www.uniprot.org/uniprotkb/O60287) carries no function annotation.

**Summary**, from NCBI Gene [9875](https://www.ncbi.nlm.nih.gov/gene/9875):

> Enables RNA binding activity. Predicted to be involved in maturation of 5.8S rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA) and maturation of LSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Located in fibrillar center. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17344](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17344) · Entrez [9875](https://www.ncbi.nlm.nih.gov/gene/9875) · UniProt [O60287](https://www.uniprot.org/uniprotkb/O60287) · Ensembl [ENSG00000142207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142207)

## Data

Gene col 6607: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6607); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6607, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6607]; `tensor/DDL_lfc|DDL_z.npy` [6607]; `embed/gene_vectors.npy` [6607]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6607 or target_col == 6607). Every well: [[URB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/URB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
