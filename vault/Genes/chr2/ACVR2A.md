---
symbol: "ACVR2A"
type: "gene"
col: 4313
ensembl_id: "ENSG00000121989"
name: "activin A receptor type 2A"
location: "2q22.3-q23.1"
module: 24
arm: "+"
pooled_cpm: 57.78
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ACVR2A

*activin A receptor type 2A* — 2q22.3-q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +15.6, q 0e+00, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.295× (z -24.0, q 0e+00, down in 41 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.759× (z -5.7, q 2e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC14A]] (+0.58, fdr 3e-05), [[NDUFA2]] (+0.58, fdr 2e-04), [[SATB2-AS1]] (+0.58, fdr 1e-05); moves opposite to [[CLPB]] (-0.58, fdr 1e-05), [[SLC35F6]] (-0.55, fdr 3e-05), [[NPIPB4]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4313.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +15.6 | 0e+00 | 42/49 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +12.5 | 3e-33 | 45/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +12.4 | 4e-33 | 45/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +11.2 | 9e-27 | 32/48 (J82, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +10.6 | 6e-24 | 40/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +10.4 | 3e-23 | 42/48 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +9.6 | 1e-19 | 44/48 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +9.1 | 8e-18 | 37/48 (LoVo, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +6.8 | 5e-10 | 33/49 (SW480, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.8 | 5e-10 | 33/50 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +5.8 | 4e-07 | 31/49 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +5.4 | 3e-06 | 25/48 (J82, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.29×** | +5.0 | 3e-05 | 23/47 (KATO III, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +4.9 | 3e-05 | 26/49 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.8 | 6e-05 | 25/48 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.7 | 7e-05 | 19/48 (BT-474, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4313.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.295×** | -24.0 | 0e+00 | 41/42 (HT-29, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.329×** | -22.8 | 0e+00 | 44/48 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.432×** | -15.9 | 0e+00 | 37/44 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.690×** | -7.6 | 3e-12 | 30/48 (A549, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.759×** | -5.7 | 2e-06 | 26/48 (SW480, HT-29, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.766×** | -5.5 | 4e-06 | 26/48 (AsPC-1, SW48, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.884× | -3.6 | 0.025 | 8/48 (RKO, NCI-H1573, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.785×** | -3.6 | 0.026 | 15/48 (NCI-H2347, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.837× | -3.5 | 0.026 | 11/47 (SNU-423, NCI-H460, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.788×** | -3.5 | 0.026 | 20/47 (SK-MEL-2, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.842× | -3.4 | 0.032 | 14/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.720×** | -3.4 | 0.035 | 14/48 (NCI-H2347, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | 0.903× | -3.0 | 0.11 | 4/48 (NCI-H2347, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4313. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 36.7 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 44.7 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.363× (z -11.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 63.7 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -14.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 65.6 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -14.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 92.2 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -13.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 37.9 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.70× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -10.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 35.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.2) | — |
| [[SW480 (line)]] | alt | 56.7 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -12.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 50.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -13.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 36.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +14.2) | — |
| [[NCI-H2030 (line)]] | alt | 48.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.36× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 79.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -21.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 71.9 | 1 | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -13.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 106 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -14.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 110 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.0970× (z -21.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 58.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0908× (z -23.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 93.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -17.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 94.3 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.45× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -16.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 44.0 | 2 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -10.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 37.5 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.7) | [[SBI-0640756 (drug)]] 5 µM 0.0589× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 88.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -15.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 94.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.40× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | [[Dinaciclib (drug)]] 5 µM 0.185× (z -15.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +12.7) | — |
| [[SHP-77 (line)]] | alt | 113 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0714× (z -28.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 81.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -19.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 55.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -14.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 34.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -9.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 44.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -12.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 60.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0649× (z -19.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 52.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -13.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 60.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0268× (z -34.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 46.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -14.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 57.1 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.44× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 51.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.50× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -16.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -9.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 51.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -10.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 39.1 | 1 | 0 | [[Ponatinib (drug)]] 5 µM 3.08× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 57.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0812× (z -12.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -9.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4313), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC14A]] | +0.58 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[NDUFA2]] | +0.58 | +0.32 / +0.65 | both halves | 2e-04 |  |
| [[SATB2-AS1]] | +0.58 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[NUP54]] | +0.58 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[FGFR1OP2]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[NEK7]] | +0.57 | +0.61 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[PAPOLG]] | +0.56 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[KATNA1]] | +0.56 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[TBPL1]] | +0.56 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[CUL3]] | +0.55 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[TRIM7-AS2]] | +0.55 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[TAPT1]] | +0.55 | +0.60 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLPB]] | -0.58 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[SLC35F6]] | -0.55 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[NPIPB4]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[PEPD]] | -0.54 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[HERC2P9-1]] | -0.53 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[PTPN11]] | -0.51 | -0.26 / -0.57 | both halves | 4e-04 |  |
| [[ACSF3]] | -0.51 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[GCLM]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[CHCHD3]] | -0.49 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[PSMC3]] | -0.49 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[ANKLE2]] | -0.49 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[RNF32-AS1]] | -0.49 | -0.38 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.408). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-0.7, -35.7); signed map (-22.9, 18.1). **Vector** length 92.6, 24.7% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +15.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +9.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +10.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +4.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.6 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +5.8 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.5 | +1.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.4 | +0.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.8 | -5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -24.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | activin A receptor type 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q22.3-q23.1 — chr2:147,844,517-147,930,826 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ACTRII; previously ACVR2 |
| Gene groups (HGNC) | Type 2 receptor serine/threonine kinases; BMP receptors |
| Hallmark sets | ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, UV_RESPONSE_DN |
| Reactome | 7 pathways, smallest: Regulation of signaling by NODAL; TGFBR3 regulates activin signaling; Signaling by NODAL |
| Matched by | ensembl_id |

**Function**, from UniProt [P27037](https://www.uniprot.org/uniprotkb/P27037) (Activin receptor type-2A):

> On ligand binding, forms a receptor complex consisting of two type II and two type I transmembrane serine/threonine kinases. Type II receptors phosphorylate and activate type I receptors which autophosphorylate, then bind and activate SMAD transcriptional regulators. Receptor for activin A, activin B and inhibin A. Mediates induction of adipogenesis by GDF6 (By similarity).

**Summary**, from NCBI Gene [92](https://www.ncbi.nlm.nih.gov/gene/92):

> This gene encodes a receptor that mediates the functions of activins, which are members of the transforming growth factor-beta (TGF-beta) superfamily involved in diverse biological processes. The encoded protein is a transmembrane serine-threonine kinase receptor which mediates signaling by forming heterodimeric complexes with various combinations of type I and type II receptors and ligands in a cell-specific manner. The encoded type II receptor is primarily involved in ligand-binding and …

**Accessions** — [HGNC:173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:173) · Entrez [92](https://www.ncbi.nlm.nih.gov/gene/92) · UniProt [P27037](https://www.uniprot.org/uniprotkb/P27037) · Ensembl [ENSG00000121989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121989)

## Data

Gene col 4313: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4313); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4313, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4313]; `tensor/DDL_lfc|DDL_z.npy` [4313]; `embed/gene_vectors.npy` [4313]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4313 or target_col == 4313). Every well: [[ACVR2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACVR2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
