---
symbol: "PPP1R3B"
type: "gene"
col: 10371
ensembl_id: "ENSG00000173281"
name: "protein phosphatase 1 regulatory subunit 3B"
location: "8p23.1"
module: 79
arm: "+"
pooled_cpm: 41.57
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 37
n_dd_up_clean: 5
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# PPP1R3B

*protein phosphatase 1 regulatory subunit 3B* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.38× (z +5.2, q 1e-04, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.372× (z -22.7, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAPC1]] (+0.70, fdr 7e-06), [[TXNIP]] (+0.65, fdr 1e-05), [[IRF2BP2]] (+0.63, fdr 1e-05); moves opposite to [[MACROH2A1]] (-0.55, fdr 2e-05), [[ZNF731P]] (-0.55, fdr 2e-05), [[MFSD14B]] (-0.54, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LNX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10371.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +5.2 | 1e-04 | 28/46 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +4.9 | 2e-04 | 21/45 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +4.9 | 2e-04 | 24/45 (RKO, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +4.5 | 0.001 | 24/47 (NCI-H1792, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.9 | 0.012 | 20/46 (KATO III, Panc 03.27, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.26×** | +3.6 | 0.034 | 16/47 (LS 180, KATO III, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.054 | 13/45 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.069 | 14/46 (AsPC-1, Hs 766T, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10371.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.372×** | -22.7 | 0e+00 | 43/46 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.374×** | -15.4 | 0e+00 | 39/45 (H4, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.406×** | -14.6 | 0e+00 | 44/46 (NCI-H1792, RKO, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.403×** | -14.2 | 1e-43 | 44/46 (NCI-H23, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.461×** | -12.6 | 3e-34 | 40/46 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.471×** | -12.2 | 2e-32 | 35/44 (RKO, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.482×** | -11.9 | 1e-30 | 41/46 (COLO 205, RKO, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.473×** | -11.7 | 1e-29 | 31/37 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.500×** | -10.8 | 2e-25 | 39/47 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.542×** | -10.0 | 1e-21 | 38/46 (RKO, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.575×** | -8.5 | 1e-15 | 37/46 (HT-29, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.606×** | -8.1 | 2e-14 | 38/46 (RKO, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.628×** | -7.6 | 2e-12 | 27/46 (H4, SW 900, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.757×** | -6.4 | 7e-09 | 26/47 (Hs 766T, NCI-H1792, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.761×** | -6.2 | 2e-08 | 25/46 (A-172, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.673×** | -6.2 | 2e-08 | 24/46 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.695×** | -5.6 | 6e-07 | 24/44 (COLO 205, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.728×** | -5.2 | 7e-06 | 25/46 (H4, HCT15, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.829×** | -4.3 | 4e-04 | 24/45 (NCI-H1792, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.770×** | -4.0 | 0.001 | 22/46 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.846× | -3.8 | 0.003 | 20/47 (CFPAC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.798×** | -3.7 | 0.005 | 20/46 (NCI-H460, SW 1088, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.731×** | -3.6 | 0.005 | 17/47 (NCI-H460, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.798×** | -3.5 | 0.009 | 16/46 (CHP-212, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.63 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10371. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.8 | 0 | 14 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0754× (z -24.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -23.6) |
| [[RKO (line)]] | wt | 109 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -28.9) |
| [[NCI-H1792 (line)]] | alt | 96.2 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -27.6) |
| [[H4 (line)]] | wt | 50.2 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -16.5) |
| [[A-172 (line)]] | wt | 99.0 | 1 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -14.1) |
| [[RPMI-7951 (line)]] | alt | 68.0 | 0 | 8 (7 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.179× (z -13.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -12.5) |
| [[PANC-1 (line)]] | alt | 25.6 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -18.5) |
| [[A498 (line)]] | wt | 54.6 | 1 (1 ⚠) | 5 (3 ⚠) | [[Selinexor (drug)]] 5 µM 2.09× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -14.0) |
| [[HT-29 (line)]] | alt | 39.5 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -13.9) |
| [[SHP-77 (line)]] | alt | 70.8 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.266× (z -13.9) |
| [[SK-MEL-2 (line)]] | alt | 67.7 | 1 (1 ⚠) | 5 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.80× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -16.7) |
| [[SW480 (line)]] | alt | 16.5 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -12.7) |
| [[COLO 205 (line)]] | alt | 81.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 32.5 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 30.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -20.1) |
| [[CFPAC-1 (line)]] | alt | 80.1 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -11.4) |
| [[HCT15 (line)]] | alt | 68.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0734× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 26.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.2) |
| [[HOP62 (line)]] | alt | 35.4 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -14.4) |
| [[Hs 766T (line)]] | wt | 56.6 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.212× (z -11.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -11.1) |
| [[LoVo (line)]] | wt | 40.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A549 (line)]] | wt | 42.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 52.3 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.233× (z -10.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -10.5) |
| [[C32 (line)]] | wt | 34.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -10.1) |
| [[HS-578T (line)]] | alt | 38.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -16.8) |
| [[KATO III (line)]] | alt | 59.8 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -13.0) |
| [[SW1417 (line)]] | alt | 27.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -11.8) |
| [[A-427 (line)]] | wt | 12.2 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 19.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -9.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -8.5) |
| [[LS 180 (line)]] | wt | 44.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0993× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[NCI-H23 (line)]] | alt | 29.3 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0877× (z -17.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 48.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -14.1) |
| [[SW 900 (line)]] | alt | 40.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -9.8) |
| [[CHP-212 (line)]] | wt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 48.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -12.1) |
| [[SNU-1 (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0721× (z -11.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 32.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -9.1) |
| [[AN3 CA (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.32 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10371), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPC1]] | +0.70 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[TXNIP]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[IRF2BP2]] | +0.63 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[ADM]] | +0.62 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[FOSL2]] | +0.61 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[MFAP1]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[BIRC3]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ZNF292]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[DEPP1]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[MRFAP1L1]] | +0.57 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[BTG1]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CSTF1]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACROH2A1]] | -0.55 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[ZNF731P]] | -0.55 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[MFSD14B]] | -0.54 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[LRP8]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[NPLOC4]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[FAM20B]] | -0.52 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[NECAB3]] | -0.51 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[NIPA2]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[SELENOI]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[MAPK9]] | -0.51 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[ECPAS]] | -0.51 | -0.56 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LNX1]] | B | LNX1 activity raises PPP1R3B's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.85× lower at baseline in the lines without LNX1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[DEPP1]] | B | DEPP1 activity raises PPP1R3B's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 1.53× lower at baseline in the lines without DEPP1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[ETS2]] | B | ETS2 activity raises PPP1R3B's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.16× lower at baseline in the lines without ETS2 | 0.041 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[TXNIP]] | B | TXNIP activity raises PPP1R3B's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without TXNIP | 0.044 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises PPP1R3B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RND3]] | B | RND3 activity raises PPP1R3B's level | lines that do not express RND3 (5) vs lines expressing it (45) | 2.99× lower at baseline in the lines without RND3 | 0.060 | ⚠ within organs, on part of the lines; also absent: GULP1, SFXN3, GALNT7; its own permutation p |
| [[ACKR3]] | B | ACKR3 activity raises PPP1R3B's level | lines that do not express ACKR3 (30) vs lines expressing it (20) | 1.54× lower at baseline in the lines without ACKR3 | 0.070 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1 |
| [[SP140L]] | B | SP140L activity raises PPP1R3B's level | lines that do not express SP140L (5) vs lines expressing it (45) | 2.83× lower at baseline in the lines without SP140L | 0.080 | ⚠ within organs, on part of the lines; also absent: RNASEL, SP100, ALCAM; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.470). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.0, -4.9); signed map (-3.9, 11.7). **Vector** length 109, 31.2% of its response variance represented; |z| ≥ 3 in 1,342 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.4 | +4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +4.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.6 | -14.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.4 | -12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -5.2 | -11.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.0 | -15.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -4.9 | -12.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -8.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.1 | -6.4 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -2.5 | -0.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.3 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:9,136,255-9,151,574 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GL, FLJ14005, PPP1R4 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XI6](https://www.uniprot.org/uniprotkb/Q86XI6) (Protein phosphatase 1 regulatory subunit 3B):

> Acts as a glycogen-targeting subunit for phosphatase PP1. Facilitates interaction of the PP1 with enzymes of the glycogen metabolism and regulates its activity. Suppresses the rate at which PP1 dephosphorylates (inactivates) glycogen phosphorylase and enhances the rate at which it activates glycogen synthase and therefore limits glycogen breakdown. Its activity is inhibited by PYGL, resulting in inhibition of the glycogen synthase and glycogen phosphorylase phosphatase activities of PP1. …

**Summary**, from NCBI Gene [79660](https://www.ncbi.nlm.nih.gov/gene/79660):

> This gene encodes the catalytic subunit of the serine/theonine phosphatase, protein phosphatase-1. The encoded protein is expressed in liver and skeletal muscle tissue and may be involved in regulating glycogen synthesis in these tissues. This gene may be a involved in type 2 diabetes and maturity-onset diabetes of the young. Alternate splicing results in multiple transcript variants that encode the same protein.[provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:14942](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14942) · Entrez [79660](https://www.ncbi.nlm.nih.gov/gene/79660) · UniProt [Q86XI6](https://www.uniprot.org/uniprotkb/Q86XI6) · Ensembl [ENSG00000173281](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173281)

## Data

Gene col 10371: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10371); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10371, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10371]; `tensor/DDL_lfc|DDL_z.npy` [10371]; `embed/gene_vectors.npy` [10371]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10371 or target_col == 10371). Every well: [[PPP1R3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
