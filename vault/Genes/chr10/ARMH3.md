---
symbol: "ARMH3"
type: "gene"
col: 4150
ensembl_id: "ENSG00000120029"
name: "armadillo like helical domain containing 3"
location: "10q24.32"
module: 169
arm: "+"
pooled_cpm: 98.13
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# ARMH3

*armadillo like helical domain containing 3* — 10q24.32

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.422× (z -25.5, q 0e+00, down in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.484× (z -16.8, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFATC3]] (+0.66, fdr 1e-05), [[SEC24B]] (+0.60, fdr 2e-05), [[TYW1]] (+0.60, fdr 1e-05); moves opposite to [[CGGBP1]] (-0.60, fdr 1e-05), [[AXL]] (-0.58, fdr 1e-05), [[KDSR]] (-0.56, fdr 2e-05).
> It is in [[Module 169]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4150.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.9 | 0.053 | 0/50 | inconsistent across doses | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 1.11× | +3.0 | 0.36 | 3/48 (MIA PaCa-2, SNU-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.19× | +3.0 | 0.36 | 12/50 (LOX-IMVI, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 18 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4150.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.422×** | -25.5 | 0e+00 | 47/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.429×** | -18.9 | 0e+00 | 46/48 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.484×** | -16.8 | 0e+00 | 42/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.487×** | -16.0 | 0e+00 | 41/44 (Panc 03.27, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.507×** | -15.7 | 0e+00 | 43/49 (C32, NCI-H2030, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.474×** | -15.3 | 0e+00 | 41/45 (Panc 03.27, C32, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.582×** | -12.1 | 1e-31 | 39/50 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.669×** | -12.0 | 2e-31 | 39/49 (AsPC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.643×** | -9.8 | 4e-21 | 35/48 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.687×** | -8.7 | 2e-16 | 38/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.693×** | -8.5 | 9e-16 | 34/48 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.693×** | -8.5 | 9e-16 | 38/48 (NCI-H2030, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.731×** | -7.3 | 2e-11 | 31/48 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.732×** | -7.0 | 1e-10 | 33/47 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **0.736×** | -6.8 | 3e-10 | 34/47 (SNU-423, C32, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.828×** | -4.9 | 2e-05 | 24/48 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.871× | -3.2 | 0.033 | 16/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.738×** | -3.1 | 0.041 | 14/49 (NCI-H1573, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4150. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 141 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -24.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -15.8) |
| [[C32 (line)]] | wt | 117 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -17.2) |
| [[MIA PaCa-2 (line)]] | alt | 112 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -20.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.399× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 112 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -17.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.336× (z -16.0) |
| [[HOP62 (line)]] | alt | 118 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -24.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -17.0) |
| [[LOX-IMVI (line)]] | wt | 113 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -18.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 131 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.483× (z -9.9) |
| [[A-172 (line)]] | wt | 83.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -13.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -13.4) |
| [[HS-578T (line)]] | alt | 75.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -14.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 114 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -25.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -20.3) |
| [[CFPAC-1 (line)]] | alt | 88.3 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -26.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 87.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -12.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.459× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 97.3 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.431× (z -9.7) |
| [[SW1417 (line)]] | alt | 90.0 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -14.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -8.6) |
| [[A549 (line)]] | wt | 104 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.425× (z -11.4) |
| [[LS 180 (line)]] | wt | 87.8 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.403× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 92.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -12.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -9.3) |
| [[A-427 (line)]] | wt | 90.9 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -15.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 81.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -17.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -13.4) |
| [[hTERT-HPNE (line)]] | wt | 75.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -11.5) |
| [[PANC-1 (line)]] | alt | 125 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -21.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -16.6) |
| [[SNU-1 (line)]] | wt | 120 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -10.5) |
| [[SW 900 (line)]] | alt | 104 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -16.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.422× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 59.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -14.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 89.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -10.1) |
| [[SW480 (line)]] | alt | 101 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.472× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -10.2) |
| [[AN3 CA (line)]] | alt | 186 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -12.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.319× (z -9.0) |
| [[BT-474 (line)]] | alt | 56.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -12.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[COLO 205 (line)]] | alt | 108 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -20.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[H4 (line)]] | wt | 88.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 85.9 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.345× (z -12.5) |
| [[J82 (line)]] | alt | 57.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -14.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.2) |
| [[LoVo (line)]] | wt | 97.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -15.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.459× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 88.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HCT15 (line)]] | alt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HepG2_C3A (line)]] | wt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[Hs 766T (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[KATO III (line)]] | alt | 90.8 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.469× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~63% of this change |
| [[A498 (line)]] | wt | 72.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -9.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[CHP-212 (line)]] | wt | 92.3 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.220× (z -9.1) |
| [[RKO (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.420× (z -8.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 81.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H2122 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4150), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFATC3]] | +0.66 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[SEC24B]] | +0.60 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[TYW1]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[RBM6]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[UBAC2]] | +0.59 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[EYA3]] | +0.58 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[DEPDC5]] | +0.58 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CRYZL1]] | +0.58 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[IPO11]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.58 | +0.61 / +0.44 | both halves | 3e-05 | same gene group |
| [[MRPL34]] | +0.58 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[CTNNBL1]] | +0.57 | +0.62 / +0.49 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGGBP1]] | -0.60 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[AXL]] | -0.58 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[KDSR]] | -0.56 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[RO60]] | -0.55 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[HIVEP2]] | -0.54 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[THAP9]] | -0.53 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[NOTCH2NLB]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SLC30A1]] | -0.52 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[SKIL]] | -0.52 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[PAN2]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[KDM6B]] | -0.51 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[ARCN1]] | -0.51 | -0.57 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARMH3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.4, -18.0); signed map (-49.7, -19.2). **Vector** length 76.0, 20.4% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.3 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +1.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +0.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +0.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | -1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.1 | -25.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -16.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.3 | -18.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -12.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | armadillo like helical domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:101,845,599-102,056,193 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13114, DGARM; previously C10orf76 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T2E6](https://www.uniprot.org/uniprotkb/Q5T2E6) (Armadillo-like helical domain-containing protein 3):

> Involved in GBF1 recruitment, Golgi maintenance and protein secretion.

**Summary**, from NCBI Gene [79591](https://www.ncbi.nlm.nih.gov/gene/79591):

> Involved in regulation of Golgi organization. Located in Golgi membrane and cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25788) · Entrez [79591](https://www.ncbi.nlm.nih.gov/gene/79591) · UniProt [Q5T2E6](https://www.uniprot.org/uniprotkb/Q5T2E6) · Ensembl [ENSG00000120029](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120029)

## Data

Gene col 4150: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4150); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4150, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4150]; `tensor/DDL_lfc|DDL_z.npy` [4150]; `embed/gene_vectors.npy` [4150]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4150 or target_col == 4150). Every well: [[ARMH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
