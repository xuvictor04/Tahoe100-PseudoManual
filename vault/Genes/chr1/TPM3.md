---
symbol: "TPM3"
type: "gene"
col: 6768
ensembl_id: "ENSG00000143549"
name: "tropomyosin 3"
location: "1q21.3"
module: 78
arm: "+"
pooled_cpm: 352.51
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# TPM3

*tropomyosin 3* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.22× (z +23.7, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.66× (z +8.3, q 6e-15, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.05 µM: 0.805× (z -4.9, q 5e-04, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCAP31]] (+0.76, fdr 7e-06), [[MSN]] (+0.70, fdr 7e-06), [[CAP1]] (+0.70, fdr 7e-06); moves opposite to [[LIPT1]] (-0.67, fdr 7e-06), [[RAB9A]] (-0.65, fdr 7e-06), [[SAT2]] (-0.63, fdr 7e-06).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CAP1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 19 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6768.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.22×** | +23.7 | 0e+00 | 49/49 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.91×** | +21.6 | 0e+00 | 44/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.88×** | +16.1 | 0e+00 | 45/45 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.49×** | +9.2 | 3e-18 | 42/49 (NCI-H2347, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.74×** | +9.2 | 5e-18 | 46/48 (SW1417, Panc 03.27, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.70×** | +8.7 | 2e-16 | 48/48 (SW1417, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.67×** | +8.5 | 2e-15 | 44/48 (SW1417, NCI-H460, …) | two highest doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +8.3 | 6e-15 | 45/48 (SW480, HT-29, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +6.9 | 3e-10 | 41/48 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +6.8 | 6e-10 | 43/48 (Panc 03.27, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.44×** | +5.8 | 3e-07 | 33/50 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | **1.36×** | +4.9 | 4e-05 | 36/47 (C32, SW48, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.4 | 4e-04 | 31/38 (NCI-H2347, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.002 | 35/48 (NCI-H460, A549, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.26×** | +3.9 | 0.004 | 34/47 (NCI-H460, SW 900, …) | two highest doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.005 | 32/48 (HT-29, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.023 | 26/48 (SK-MEL-2, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.037 | 23/48 (RKO, SNU-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6768.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **0.805×** | -4.9 | 5e-04 | 32/48 (Hs 766T, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.731×** | -4.7 | 5e-04 | 36/50 (NCI-H23, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.818×** | -4.7 | 5e-04 | 33/48 (SW1417, J82, …) | rises with dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.755×** | -4.6 | 5e-04 | 46/49 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.675×** | -4.6 | 5e-04 | 40/47 (SHP-77, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.785×** | -3.8 | 0.013 | 29/47 (NCI-H23, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.796×** | -3.6 | 0.027 | 29/48 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.859× | -3.5 | 0.029 | 12/48 (A-427, Hs 766T, …) | inconsistent across doses |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **0.807×** | -3.5 | 0.029 | 29/48 (KATO III, SW1417, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.813×** | -3.4 | 0.040 | 24/48 (A-172, KATO III, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.851× | -3.3 | 0.055 | 19/48 (AsPC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.2 | 0.067 | 23/48 (A-427, H4, …) | rises with dose | composition shift; position effect removed |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.827×** | -3.1 | 0.082 | 21/48 (HEC-1-A, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Allantoin (drug)]] 0.5 µM |  | **0.833×** | -3.0 | 0.098 | 22/48 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.820×** | -3.0 | 0.098 | 23/48 (AsPC-1, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.875× | -3.0 | 0.098 | 15/49 (SW480, CFPAC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6768. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 337 | 14 (14 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.18× (z +19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 173 | 8 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.88× (z +20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Panc 03.27 (line)]] | alt | 266 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.24× (z +10.2) | — |
| [[C32 (line)]] | wt | 183 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.51× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 239 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.46× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 257 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 269 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.60× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 304 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.13× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 395 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 285 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LOX-IMVI (line)]] | wt | 355 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2347 (line)]] | alt | 476 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 266 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 504 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 477 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -16.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 363 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[H4 (line)]] | wt | 351 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 193 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HT-29 (line)]] | alt | 326 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.03× (z +9.1) | — |
| [[KATO III (line)]] | alt | 252 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 253 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 762 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.572× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 475 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 195 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.66× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[AsPC-1 (line)]] | alt | 594 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 220 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[CFPAC-1 (line)]] | alt | 395 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[CHP-212 (line)]] | wt | 217 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 340 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Hs 766T (line)]] | wt | 442 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HS-578T (line)]] | alt | 214 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 300 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 457 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 336 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 688 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 318 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RPMI-7951 (line)]] | alt | 287 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 408 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-1 (line)]] | wt | 167 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.27× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW 900 (line)]] | alt | 345 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW48 (line)]] | wt | 252 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.00× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 226 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HCT15 (line)]] | alt | 346 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 323 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1573 (line)]] | alt | 300 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW 1271 (line)]] | alt | 221 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2122 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 306 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 319 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6768), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | +0.76 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[MSN]] | +0.70 | +0.76 / +0.66 | both halves | 7e-06 | pathway: Signaling by ALK fusions and activated point mutants; STRING 647 |
| [[CAP1]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 | STRING 474 |
| [[IQGAP1]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 | pathway: RHOV GTPase cycle; STRING 564 |
| [[RALB]] | +0.68 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[PSMD2]] | +0.66 | +0.67 / +0.57 | both halves | 8e-06 |  |
| [[HSPA8]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[RECQL]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[NES]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ZNF731P]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ITGB1]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MYOGENESIS |
| [[CDC37]] | +0.61 | +0.39 / +0.65 | both halves | 5e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIPT1]] | -0.67 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[RAB9A]] | -0.65 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[SAT2]] | -0.63 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[PQBP1]] | -0.62 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[ANAPC16]] | -0.62 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[STAT5B]] | -0.61 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[SMDT1]] | -0.61 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[THAP3]] | -0.60 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[C1orf43]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 | ⚠ same locus (12.0 kb, same strand: neighbours can correlate without regulation) |
| [[DPH1]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[VAMP2]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[SNHG8]] | -0.57 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[RNF115]] | -0.57 | -0.60 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAP1]] | C | CAP1's natural level weakens TPM3's drug response | CAP1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.10; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.5, 10.1); signed map (-8.3, 38.8). **Vector** length 130, 54.8% of its response variance represented; |z| ≥ 3 in 1,480 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *apical junction* (hallmark, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +5.4 | +9.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +5.3 | +8.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.1 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +6.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +1.7 |
|  | [[Decitabine (drug)]] 5 µM |  | +2.6 | +0.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -9.3 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.0 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.1 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.5 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.1 | -2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -4.8 | -4.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -4.5 | -1.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.0 | -4.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -4.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | tropomyosin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,155,308-154,194,648 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRK; previously NEM1 |
| Gene groups (HGNC) | Tropomyosins |
| Hallmark sets | MYOGENESIS |
| Reactome | 10 pathways, smallest: Striated Muscle Contraction; RHOV GTPase cycle; Smooth Muscle Contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P06753](https://www.uniprot.org/uniprotkb/P06753) (Tropomyosin alpha-3 chain):

> Binds to actin filaments in muscle and non-muscle cells. Plays a central role, in association with the troponin complex, in the calcium dependent regulation of vertebrate striated muscle contraction. Smooth muscle contraction is regulated by interaction with caldesmon. In non-muscle cells is implicated in stabilizing cytoskeleton actin filaments.

**Summary**, from NCBI Gene [7170](https://www.ncbi.nlm.nih.gov/gene/7170):

> This gene encodes a member of the tropomyosin family of actin-binding proteins. Tropomyosins are dimers of coiled-coil proteins that provide stability to actin filaments and regulate access of other actin-binding proteins. Mutations in this gene result in autosomal dominant nemaline myopathy and other muscle disorders. This locus is involved in translocations with other loci, including anaplastic lymphoma receptor tyrosine kinase (ALK) and neurotrophic tyrosine kinase receptor type 1 (NTRK1), …

**Accessions** — [HGNC:12012](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12012) · Entrez [7170](https://www.ncbi.nlm.nih.gov/gene/7170) · UniProt [P06753](https://www.uniprot.org/uniprotkb/P06753) · Ensembl [ENSG00000143549](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143549)

## Data

Gene col 6768: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6768); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6768, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6768]; `tensor/DDL_lfc|DDL_z.npy` [6768]; `embed/gene_vectors.npy` [6768]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6768 or target_col == 6768). Every well: [[TPM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
