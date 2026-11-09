---
symbol: "ARL6IP6"
type: "gene"
col: 10876
ensembl_id: "ENSG00000177917"
name: "ARF like GTPase 6 interacting protein 6"
location: "2q23.3"
module: 6
arm: "+"
pooled_cpm: 48.8
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 25
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ARL6IP6

*ARF like GTPase 6 interacting protein 6* — 2q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.94× (z +10.3, q 4e-22, up in 37 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.83× (z +9.4, q 1e-18, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.436× (z -18.2, q 0e+00, down in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.398× (z -14.3, q 5e-44, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAPG2]] (+0.61, fdr 1e-05), [[MSH5]] (+0.60, fdr 3e-05), [[FN3KRP]] (+0.60, fdr 3e-05); moves opposite to [[IGHMBP2]] (-0.59, fdr 6e-05), [[TMEM101]] (-0.58, fdr 7e-05), [[MSX1]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10876.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +10.3 | 4e-22 | 37/46 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +9.4 | 1e-18 | 43/48 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +9.0 | 6e-17 | 29/38 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +8.2 | 5e-14 | 29/41 (MIA PaCa-2, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +8.0 | 1e-13 | 39/48 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +6.9 | 5e-10 | 36/48 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.22× | +3.0 | 0.20 | 14/48 (HEC-1-A, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10876.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.436×** | -18.2 | 0e+00 | 46/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.398×** | -14.3 | 5e-44 | 45/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.414×** | -13.7 | 2e-40 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.442×** | -12.7 | 8e-35 | 42/48 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.443×** | -12.7 | 1e-34 | 42/48 (SW480, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.468×** | -11.1 | 7e-27 | 45/48 (KATO III, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.484×** | -10.9 | 1e-25 | 39/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.504×** | -10.7 | 1e-24 | 43/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.524×** | -10.0 | 6e-22 | 34/47 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.348×** | -8.6 | 5e-16 | 40/49 (A-427, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.611×** | -7.7 | 1e-12 | 36/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.617×** | -7.5 | 3e-12 | 38/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.606×** | -7.5 | 3e-12 | 38/47 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.425×** | -6.9 | 2e-10 | 34/43 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.477×** | -6.0 | 7e-08 | 33/47 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.698×** | -5.6 | 8e-07 | 28/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.617×** | -5.4 | 3e-06 | 35/48 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.788×** | -5.2 | 5e-06 | 30/48 (HEC-1-A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.576×** | -4.5 | 2e-04 | 30/48 (LOX-IMVI, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10876. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 61.2 | 2 (2 ⚠) | 14 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +14.7) ⚠ toxic; transcription drop | [[Auranofin (drug)]] 5 µM 0.217× (z -18.7) |
| [[HEC-1-A (line)]] | alt | 74.9 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -22.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.210× (z -17.6) |
| [[LoVo (line)]] | wt | 41.4 | 1 (1 ⚠) | 9 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.49× (z +9.4) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -13.3) |
| [[PANC-1 (line)]] | alt | 67.2 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -22.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.239× (z -19.3) |
| [[KATO III (line)]] | alt | 50.9 | 0 | 9 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.190× (z -14.7) |
| [[HCT15 (line)]] | alt | 64.5 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 24.0 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.144× (z -15.2) |
| [[A-172 (line)]] | wt | 74.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -20.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.367× (z -10.4) |
| [[HOP62 (line)]] | alt | 61.6 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -15.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 65.8 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +13.8) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.331× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 46.4 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 7.07× (z +17.8) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -12.3) |
| [[SW 900 (line)]] | alt | 34.5 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +10.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.241× (z -10.0) |
| [[A-427 (line)]] | wt | 55.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -21.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.115× (z -10.8) |
| [[H4 (line)]] | wt | 54.0 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +10.2) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.159× (z -11.6) |
| [[Hs 766T (line)]] | wt | 36.0 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -9.6) |
| [[HT-29 (line)]] | alt | 29.3 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -12.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -11.7) |
| [[J82 (line)]] | alt | 74.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -14.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.322× (z -11.7) |
| [[A549 (line)]] | wt | 60.3 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -16.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.281× (z -10.8) |
| [[COLO 205 (line)]] | alt | 40.3 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0992× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -13.2) |
| [[A498 (line)]] | wt | 62.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -16.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 47.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 59.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -11.6) |
| [[LS 180 (line)]] | wt | 30.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +10.1) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -10.2) |
| [[SNU-1 (line)]] | wt | 28.8 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.132× (z -10.2) |
| [[BT-474 (line)]] | alt | 34.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.210× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 28.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.354× (z -8.6) |
| [[HS-578T (line)]] | alt | 35.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 48.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.281× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 36.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 51.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -10.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 33.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -11.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.402× (z -9.2) |
| [[SNU-423 (line)]] | alt | 41.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.338× (z -9.0) |
| [[SW1417 (line)]] | alt | 39.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -11.1) |
| [[C-33 A (line)]] | alt | 79.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.356× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 32.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 71.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -10.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -16.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RKO (line)]] | wt | 31.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -9.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 50.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SK-MEL-2 (line)]] | alt | 33.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.202× (z -11.0) |
| [[SW48 (line)]] | wt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 8.93× (z +10.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10876), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAPG2]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[MSH5]] | +0.60 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[FN3KRP]] | +0.60 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[CDK2]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[MAPK1]] | +0.57 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[ERI1]] | +0.56 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[CENPK]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[MZT1]] | +0.56 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[GNB1]] | +0.56 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[GUSB]] | +0.55 | +0.37 / +0.45 | both halves | 8e-05 |  |
| [[CENPI]] | +0.55 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[RBBP7]] | +0.55 | +0.40 / +0.55 | both halves | 5e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGHMBP2]] | -0.59 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[TMEM101]] | -0.58 | -0.37 / -0.55 | both halves | 7e-05 |  |
| [[MSX1]] | -0.56 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[CCDC117]] | -0.56 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[RHBDD3]] | -0.55 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[SLC4A1AP]] | -0.55 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[FDX2]] | -0.54 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[COA6]] | -0.54 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[PBDC1]] | -0.54 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[CCDC59]] | -0.54 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[BAG3]] | -0.53 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[RPP25L]] | -0.52 | -0.28 / -0.46 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ARL6IP6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-28.9, -45.0); signed map (-36.0, -39.2). **Vector** length 92.3, 27.6% of its response variance represented; |z| ≥ 3 in 1,324 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.6 | +6.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.3 | +9.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +8.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.3 | -7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +10.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +0.8 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | +1.8 | +0.3 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | +1.7 | +1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.6 | +0.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.5 | -12.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.8 | -11.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -6.6 | -6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.7 | -18.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -10.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.6 | -5.4 |
|  | [[Infigratinib (drug)]] 5 µM |  | -2.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 6 interacting protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.3 — chr2:152,717,647-152,762,396 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33864 |
| Matched by | ensembl_id |

UniProt [Q8N6S5](https://www.uniprot.org/uniprotkb/Q8N6S5) carries no function annotation.

**Summary**, from NCBI Gene [151188](https://www.ncbi.nlm.nih.gov/gene/151188):

> Predicted to be located in nuclear inner membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24048](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24048) · Entrez [151188](https://www.ncbi.nlm.nih.gov/gene/151188) · UniProt [Q8N6S5](https://www.uniprot.org/uniprotkb/Q8N6S5) · Ensembl [ENSG00000177917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177917)

## Data

Gene col 10876: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10876); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10876, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10876]; `tensor/DDL_lfc|DDL_z.npy` [10876]; `embed/gene_vectors.npy` [10876]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10876 or target_col == 10876). Every well: [[ARL6IP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL6IP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
