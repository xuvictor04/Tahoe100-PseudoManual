---
symbol: "FBXL4"
type: "gene"
col: 3339
ensembl_id: "ENSG00000112234"
name: "F-box and leucine rich repeat protein 4"
location: "6q16.1-q16.2"
module: 18
arm: "+"
pooled_cpm: 87.67
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 32
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# FBXL4

*F-box and leucine rich repeat protein 4* — 6q16.1-q16.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.257× (z -29.0, q 0e+00, down in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.385× (z -14.4, q 4e-45, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTFMT]] (+0.66, fdr 1e-05), [[SFXN4]] (+0.65, fdr 7e-06), [[CMC1]] (+0.63, fdr 7e-06); moves opposite to [[CCDC144CP]] (-0.52, fdr 4e-05), [[PIPOX]] (-0.52, fdr 3e-05), [[TRIM69]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DUXAP10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3339.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.23× | +3.2 | 0.46 | 18/48 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.48× | +3.2 | 0.46 | 19/50 (HEC-1-A, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 19 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3339.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.257×** | -29.0 | 0e+00 | 48/48 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.285×** | -18.3 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.326×** | -16.9 | 0e+00 | 43/48 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.337×** | -16.5 | 0e+00 | 45/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.385×** | -14.4 | 4e-45 | 47/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.393×** | -14.1 | 3e-43 | 44/49 (NCI-H23, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.379×** | -14.1 | 4e-43 | 41/44 (HEC-1-A, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.370×** | -13.9 | 5e-42 | 42/45 (HEC-1-A, RKO, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.182×** | -13.5 | 1e-39 | 48/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -12.1 | 4e-32 | 42/49 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.438×** | -12.0 | 2e-31 | 46/47 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.498×** | -10.5 | 4e-24 | 43/48 (SNU-423, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.506×** | -10.3 | 4e-23 | 38/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.540×** | -9.3 | 5e-19 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.598×** | -7.7 | 4e-13 | 35/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.614×** | -7.3 | 7e-12 | 42/48 (SW480, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.616×** | -7.3 | 9e-12 | 39/48 (HCT15, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.405×** | -7.1 | 3e-11 | 37/48 (LOX-IMVI, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.748×** | -6.1 | 3e-08 | 36/48 (A-172, HOP62, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.566×** | -4.5 | 2e-04 | 40/48 (SNU-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.765×** | -3.8 | 0.003 | 25/48 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.707×** | -3.7 | 0.004 | 29/48 (LoVo, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.638×** | -3.5 | 0.008 | 26/48 (NCI-H1792, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.674×** | -3.1 | 0.033 | 20/48 (Panc 03.27, A-172, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3339. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 201 | 0 | 17 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -31.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -23.3) |
| [[NCI-H460 (line)]] | wt | 87.1 | 0 | 17 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -29.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.160× (z -22.9) |
| [[SNU-423 (line)]] | alt | 170 | 0 | 17 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0759× (z -42.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.178× (z -20.0) |
| [[SW480 (line)]] | alt | 119 | 0 | 17 (11 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -24.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.226× (z -17.7) |
| [[HEC-1-A (line)]] | alt | 76.3 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -27.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -18.8) |
| [[HOP62 (line)]] | alt | 77.0 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -29.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.276× (z -13.7) |
| [[A-172 (line)]] | wt | 79.4 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -24.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -14.6) |
| [[J82 (line)]] | alt | 84.9 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -26.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 115 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -23.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.110× (z -12.1) |
| [[RKO (line)]] | wt | 126 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0978× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -13.7) |
| [[SNU-1 (line)]] | wt | 92.0 | 0 | 12 (10 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0960× (z -17.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.185× (z -13.1) |
| [[SW 900 (line)]] | alt | 67.9 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -18.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -11.2) |
| [[LoVo (line)]] | wt | 76.3 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0895× (z -27.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.202× (z -17.9) |
| [[PANC-1 (line)]] | alt | 146 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -32.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -16.1) |
| [[SW48 (line)]] | wt | 111 | 0 | 10 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -13.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.244× (z -10.6) |
| [[C32 (line)]] | wt | 97.2 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -23.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -17.5) |
| [[SHP-77 (line)]] | alt | 100 | 0 | 9 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -15.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.204× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 144 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -28.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.289× (z -13.4) |
| [[A549 (line)]] | wt | 80.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -24.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.269× (z -13.4) |
| [[BT-474 (line)]] | alt | 57.6 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.259× (z -11.2) |
| [[HCT15 (line)]] | alt | 103 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -18.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.175× (z -13.4) |
| [[hTERT-HPNE (line)]] | wt | 81.4 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -20.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -15.1) |
| [[RPMI-7951 (line)]] | alt | 81.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -22.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -13.7) |
| [[A498 (line)]] | wt | 59.5 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -18.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.349× (z -11.0) |
| [[AN3 CA (line)]] | alt | 110 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -15.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -13.3) |
| [[H4 (line)]] | wt | 66.7 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0718× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.261× (z -9.6) |
| [[HS-578T (line)]] | alt | 59.5 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -23.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -18.6) |
| [[HT-29 (line)]] | alt | 62.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -16.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.219× (z -13.0) |
| [[LS 180 (line)]] | wt | 65.3 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -18.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.317× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 93.9 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -24.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.127× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 86.5 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -16.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 60.6 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -20.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[C-33 A (line)]] | alt | 90.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -11.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.160× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 74.2 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -11.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 80.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -22.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[KATO III (line)]] | alt | 85.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[NCI-H1573 (line)]] | alt | 42.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -25.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -15.0) |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0742× (z -29.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.179× (z -10.1) |
| [[SW1417 (line)]] | alt | 62.8 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.512× (z -8.9) |
| [[CHP-212 (line)]] | wt | 124 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -13.9) |
| [[COLO 205 (line)]] | alt | 47.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 64.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -18.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 1271 (line)]] | alt | 111 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0722× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H2347 (line)]] | alt | 39.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -13.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 33.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -14.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 61.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -17.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.166× (z -8.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H2122 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3339), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTFMT]] | +0.66 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[SFXN4]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CMC1]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[MTX2]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[RSAD1]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[KLHL8]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ANGEL1]] | +0.60 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[DTD2]] | +0.60 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[MTERF3]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[FAM24B]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[GLMN]] | +0.59 | +0.61 / +0.57 | both halves | 8e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[WRN]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC144CP]] | -0.52 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[PIPOX]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[TRIM69]] | -0.51 | -0.55 / -0.45 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[KPTN]] | -0.50 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[SUPT6H]] | -0.50 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[B3GNT9]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ESRRB]] | -0.48 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[GPR137]] | -0.48 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[MC1R]] | -0.48 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[SLC8A2]] | -0.47 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[FER1L4]] | -0.47 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[CSNK1A1]] | -0.47 | -0.44 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUXAP10]] | B | DUXAP10 activity raises FBXL4's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without DUXAP10 | 0.073 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.537). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-5.4, -17.4); signed map (-39.2, -18.9). **Vector** length 79.8, 27.5% of its response variance represented; |z| ≥ 3 in 1,410 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | -1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | -1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +0.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.7 | +0.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -6.0 | -14.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -5.3 | -13.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -4.9 | -14.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | -10.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | +0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.1-q16.2 — chr6:98,868,535-98,948,006 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBL4, FBL5 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKA2](https://www.uniprot.org/uniprotkb/Q9UKA2) (F-box/LRR-repeat protein 4):

> Substrate-recognition component of the mitochondria-localized SCF-FBXL4 ubiquitin E3 ligase complex that plays a role in the restriction of mitophagy by controlling the degradation of BNIP3 and NIX mitophagy receptors. Rescues also mitochondrial injury through reverting hyperactivation of DRP1-mediated mitochondrial fission (By similarity).

**Summary**, from NCBI Gene [26235](https://www.ncbi.nlm.nih.gov/gene/26235):

> This gene encodes a member of the F-box protein family, which are characterized by an approximately 40 amino acid motif, the F-box. F-box proteins constitute one subunit of modular E3 ubiquitin ligase complexes, called SCF complexes, which function in phosphorylation-dependent ubiquitination. The F-box domain mediates protein-protein interactions and binds directly to S-phase kinase-associated protein 1. In addition to an F-box domain, the encoded protein contains at least 9 tandem leucine-rich …

**Accessions** — [HGNC:13601](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13601) · Entrez [26235](https://www.ncbi.nlm.nih.gov/gene/26235) · UniProt [Q9UKA2](https://www.uniprot.org/uniprotkb/Q9UKA2) · Ensembl [ENSG00000112234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112234)

## Data

Gene col 3339: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3339); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3339, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3339]; `tensor/DDL_lfc|DDL_z.npy` [3339]; `embed/gene_vectors.npy` [3339]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3339 or target_col == 3339). Every well: [[FBXL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
