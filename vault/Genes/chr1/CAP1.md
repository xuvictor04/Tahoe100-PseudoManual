---
symbol: "CAP1"
type: "gene"
col: 5187
ensembl_id: "ENSG00000131236"
name: "cyclase associated actin cytoskeleton regulatory protein 1"
location: "1p34.2"
module: 78
arm: "+"
pooled_cpm: 232.89
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# CAP1

*cyclase associated actin cytoskeleton regulatory protein 1* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.63× (z +16.1, q 0e+00, up in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.52× (z +7.0, q 5e-10, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.461× (z -17.5, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARPC2]] (+0.77, fdr 7e-06), [[STK4]] (+0.70, fdr 7e-06), [[TPM3]] (+0.70, fdr 7e-06); moves opposite to [[NFYB]] (-0.63, fdr 2e-05), [[STAT5A]] (-0.63, fdr 2e-05), [[FAM111A-DT]] (-0.62, fdr 1e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STAT5A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TPM3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5187.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.63×** | +16.1 | 0e+00 | 46/49 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +15.6 | 0e+00 | 42/44 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.74×** | +8.6 | 2e-15 | 41/45 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +7.0 | 5e-10 | 42/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.46×** | +6.3 | 3e-08 | 43/48 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +6.0 | 2e-07 | 0/50 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +4.6 | 4e-04 | 36/48 (SNU-1, HCT15, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.30×** | +4.4 | 8e-04 | 31/48 (SW480, SW48, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.28×** | +4.1 | 0.003 | 32/48 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.27×** | +3.9 | 0.005 | 28/48 (SW480, SNU-1, …) | two highest doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.25×** | +3.7 | 0.012 | 28/47 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.031 | 27/48 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.031 | 25/48 (HT-29, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5187.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.461×** | -17.5 | 0e+00 | 47/48 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.675×** | -6.6 | 1e-08 | 41/48 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.706×** | -5.0 | 1e-04 | 36/50 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.805×** | -4.9 | 2e-04 | 36/48 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.741×** | -4.8 | 2e-04 | 30/48 (AsPC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.757×** | -4.7 | 3e-04 | 34/48 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.749×** | -4.5 | 6e-04 | 36/48 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.763×** | -4.3 | 0.001 | 32/47 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.834× | -4.2 | 0.002 | 25/48 (AsPC-1, NCI-H23, …) | all doses, flat | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.807×** | -3.6 | 0.019 | 33/48 (SW1417, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.806×** | -3.5 | 0.027 | 27/49 (A549, HS-578T, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **0.759×** | -3.3 | 0.052 | 26/49 (BT-474, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.825×** | -3.2 | 0.057 | 22/47 (AsPC-1, HepG2/C3A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.820×** | -3.2 | 0.058 | 27/48 (NCI-H23, AsPC-1, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.830×** | -3.1 | 0.067 | 23/48 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.831×** | -3.1 | 0.071 | 25/49 (AsPC-1, NCI-H23, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5187. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 457 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -23.3) |
| [[SW480 (line)]] | alt | 186 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.64× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -12.8) |
| [[A-172 (line)]] | wt | 239 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -15.2) |
| [[A498 (line)]] | wt | 270 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.570× (z -9.4) |
| [[HS-578T (line)]] | alt | 344 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 238 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -9.5) |
| [[J82 (line)]] | alt | 349 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -19.2) |
| [[LOX-IMVI (line)]] | wt | 246 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 268 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -15.3) |
| [[NCI-H2030 (line)]] | alt | 302 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 366 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -17.0) |
| [[NCI-H2347 (line)]] | alt | 258 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -15.5) |
| [[PANC-1 (line)]] | alt | 253 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 278 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 274 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -11.0) |
| [[SNU-423 (line)]] | alt | 218 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -10.0) |
| [[A-427 (line)]] | wt | 266 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -17.4) |
| [[A549 (line)]] | wt | 190 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -10.2) |
| [[C-33 A (line)]] | alt | 127 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C32 (line)]] | wt | 187 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -10.4) |
| [[H4 (line)]] | wt | 253 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -13.1) |
| [[HCT15 (line)]] | alt | 190 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -11.4) |
| [[HOP62 (line)]] | alt | 227 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -11.8) |
| [[Hs 766T (line)]] | wt | 374 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -10.9) |
| [[HT-29 (line)]] | alt | 196 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 230 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -16.5) |
| [[NCI-H1792 (line)]] | alt | 139 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 323 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -14.6) |
| [[KATO III (line)]] | alt | 166 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 170 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -14.7) |
| [[LS 180 (line)]] | wt | 199 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 128 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +13.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 251 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 1.93× (z +8.5) ⚠ cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -17.0) |
| [[SHP-77 (line)]] | alt | 150 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 179 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -11.0) |
| [[SW 900 (line)]] | alt | 172 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +11.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 142 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[BT-474 (line)]] | alt | 162 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 284 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -16.8) |
| [[CHP-212 (line)]] | wt | 76.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.51× (z +10.2) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 161 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 211 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 215 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -17.3) |
| [[SW 1088 (line)]] | alt | 262 | 0 | 1 | — | [[Rifaximin (drug)]] 0.5 µM 0.228× (z -8.5) |
| [[SW1417 (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW48 (line)]] | wt | 168 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2122 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 189 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5187), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC2]] | +0.77 | +0.79 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 665 |
| [[STK4]] | +0.70 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[TPM3]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 | STRING 474 |
| [[YWHAB]] | +0.69 | +0.63 / +0.61 | both halves | 7e-06 | STRING 411 |
| [[ITGB1]] | +0.68 | +0.76 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[ACOT7]] | +0.66 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[S100A16]] | +0.66 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[EHBP1L1]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[CD59]] | +0.65 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[ACTN1]] | +0.64 | +0.66 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[BCAP31]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[MTPN]] | +0.63 | +0.68 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFYB]] | -0.63 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[STAT5A]] | -0.63 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[FAM111A-DT]] | -0.62 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[RPRD2]] | -0.62 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[STAP2]] | -0.61 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[SREK1]] | -0.61 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[ZNF428]] | -0.60 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[CLK4]] | -0.60 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[REV3L]] | -0.59 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[RAD52]] | -0.59 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[ATF5]] | -0.59 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[ZBED3]] | -0.59 | -0.61 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAT5A]] | B | STAT5A activity lowers CAP1's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.06× higher at baseline in the lines without STAT5A | 0.085 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPM3]] | C | CAP1's natural level weakens TPM3's drug response | CAP1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.10; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.0, 5.4); signed map (-8.3, 39.1). **Vector** length 132, 52.6% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +7.0 | +6.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +6.6 | +3.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +6.3 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.5 | +2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +3.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.9 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -12.1 | -17.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.8 | -6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.9 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.9 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.8 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.5 | -2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.5 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | cyclase associated actin cytoskeleton regulatory protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:40,040,233-40,072,649 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAP |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 10 pathways, smallest: Role of ABL in ROBO-SLIT signaling; Platelet degranulation; Response to elevated platelet cytosolic Ca2+ |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01518](https://www.uniprot.org/uniprotkb/Q01518) (Adenylyl cyclase-associated protein 1):

> Directly regulates filament dynamics and has been implicated in a number of complex developmental and morphological processes, including mRNA localization and the establishment of cell polarity.

**Summary**, from NCBI Gene [10487](https://www.ncbi.nlm.nih.gov/gene/10487):

> The protein encoded by this gene is related to the S. cerevisiae CAP protein, which is involved in the cyclic AMP pathway. The human protein is able to interact with other molecules of the same protein, as well as with CAP2 and actin. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:20040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20040) · Entrez [10487](https://www.ncbi.nlm.nih.gov/gene/10487) · UniProt [Q01518](https://www.uniprot.org/uniprotkb/Q01518) · Ensembl [ENSG00000131236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131236)

## Data

Gene col 5187: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5187); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5187, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5187]; `tensor/DDL_lfc|DDL_z.npy` [5187]; `embed/gene_vectors.npy` [5187]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5187 or target_col == 5187). Every well: [[CAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
