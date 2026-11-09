---
symbol: "NPHP3"
type: "gene"
col: 3514
ensembl_id: "ENSG00000113971"
name: "nephrocystin 3"
location: "3q22.1"
module: 20
arm: "-"
pooled_cpm: 72.95
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 26
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# NPHP3

*nephrocystin 3* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +6.5, q 4e-08, up in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 2.54×, LoVo 2.07×, SW480 1.55×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 2.10×, AsPC-1 2.67×; ⚠ cell-cycle shift, explains ~0% of this change); [[Betamethasone dipropionate (drug)]] 5 µM in 1 line (NCI-H1573 2.70×); [[Budesonide (drug)]] 0.05 µM in 1 line (NCI-H1573 2.50×); [[Dexamethasone (drug)]] 0.05 µM in 1 line (NCI-H1573 2.35×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.562× (z -11.8, q 2e-29, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.635× (z -10.1, q 9e-22, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF12]] (+0.66, fdr 7e-06), [[HADHB]] (+0.63, fdr 1e-05), [[TRNAU1AP]] (+0.63, fdr 7e-06); moves opposite to [[TMEM33]] (-0.60, fdr 1e-05), [[EIF5A]] (-0.58, fdr 1e-05), [[LINC02595]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TRIM58]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3514.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 2.54×, LoVo 2.07×, SW480 1.55×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 2.10×, AsPC-1 2.67×; ⚠ cell-cycle shift, explains ~0% of this change); [[Betamethasone dipropionate (drug)]] 5 µM in 1 line (NCI-H1573 2.70×); [[Budesonide (drug)]] 0.05 µM in 1 line (NCI-H1573 2.50×); [[Dexamethasone (drug)]] 0.05 µM in 1 line (NCI-H1573 2.35×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +6.5 | 4e-08 | 29/48 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.1 | 1e-04 | 20/49 (A498, AsPC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.7 | 4e-04 | 23/48 (C32, LoVo, …) | top dose only | composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.006 | 18/49 (A498, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.12× | +3.7 | 0.025 | 6/48 (MIA PaCa-2, J82, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.025 | 16/50 (AsPC-1, HOP62, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.062 | 17/48 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3514.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.562×** | -11.8 | 2e-29 | 36/44 (A-427, A-172, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.591×** | -11.2 | 9e-27 | 33/43 (Panc 03.27, NCI-H23, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -10.4 | 3e-23 | 39/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.633×** | -10.1 | 6e-22 | 37/49 (NCI-H23, SW480, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.635×** | -10.1 | 9e-22 | 36/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.636×** | -9.7 | 4e-20 | 39/47 (SNU-423, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.660×** | -8.9 | 7e-17 | 33/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.693×** | -8.1 | 3e-14 | 29/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.740×** | -6.7 | 2e-09 | 31/48 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.764×** | -6.0 | 1e-07 | 24/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.770×** | -5.8 | 4e-07 | 25/48 (A-172, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.626×** | -5.4 | 3e-06 | 26/49 (SNU-423, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.632×** | -5.3 | 5e-06 | 22/38 (HOP62, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.636×** | -5.3 | 6e-06 | 27/48 (A-427, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.796×** | -5.1 | 2e-05 | 22/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.797×** | -5.0 | 2e-05 | 22/48 (SW480, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.797×** | -5.0 | 2e-05 | 26/48 (HCT15, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -4.3 | 6e-04 | 17/48 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.830×** | -4.1 | 0.001 | 21/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.834× | -4.0 | 0.002 | 17/47 (LOX-IMVI, hTERT-HPNE, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.837× | -3.9 | 0.002 | 20/48 (SNU-1, HOP62, …) | two highest doses |  |
| [[vincristine (drug)]] 5 µM |  | **0.731×** | -3.6 | 0.007 | 16/46 (J82, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.869× | -3.0 | 0.052 | 18/48 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.773×** | -3.0 | 0.052 | 15/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3514. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 112 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.492× (z -9.8) |
| [[SNU-423 (line)]] | alt | 122 | 0 | 9 (8 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.279× (z -14.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.426× (z -10.1) |
| [[SW480 (line)]] | alt | 83.8 | 1 (1 ⚠) | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.449× (z -12.0) |
| [[A-172 (line)]] | wt | 106 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.485× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 162 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.373× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 86.6 | 5 | 2 (2 ⚠) | [[Betamethasone dipropionate (drug)]] 5 µM 2.70× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[NCI-H23 (line)]] | alt | 111 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -23.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.473× (z -8.8) |
| [[J82 (line)]] | alt | 69.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.419× (z -9.5) |
| [[PANC-1 (line)]] | alt | 105 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.376× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.399× (z -14.8) |
| [[H4 (line)]] | wt | 136 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.292× (z -11.2) ⚠ cell-cycle shift, explains ~67% of this change |
| [[hTERT-HPNE (line)]] | wt | 111 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.338× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 59.7 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.260× (z -13.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.422× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 54.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -10.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 30.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -14.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 119 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.277× (z -9.5) |
| [[A549 (line)]] | wt | 64.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -15.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 80.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[C32 (line)]] | wt | 72.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.258× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HCT15 (line)]] | alt | 112 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.259× (z -12.6) ⚠ toxic |
| [[LoVo (line)]] | wt | 46.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.217× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LOX-IMVI (line)]] | wt | 75.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.451× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.481× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 88.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 67.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -11.6) |
| [[SW 1088 (line)]] | alt | 79.7 | 0 | 2 (2 ⚠) | — | [[Daptomycin (drug)]] 0.05 µM 0.0691× (z -9.6) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 38.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 97.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.366× (z -9.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[Panc 03.27 (line)]] | alt | 82.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0724× (z -27.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW 1271 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[BT-474 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3514), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF12]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[HADHB]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[TRNAU1AP]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[AAMDC]] | +0.60 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[HMGCL]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[NBPF11]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ZNF654]] | +0.59 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[RSRP1]] | +0.58 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[DYNC2I1]] | +0.58 | +0.52 / +0.63 | both halves | 1e-05 | same gene group; pathway: Assembly of the 9+0 primary cilium |
| [[NKAP]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[DALRD3]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[GOLGA8N]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM33]] | -0.60 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[EIF5A]] | -0.58 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[LINC02595]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[VMA21]] | -0.57 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[ICMT]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ANKRD52]] | -0.55 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[MRPL42]] | -0.53 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[TFDP1]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 | pathway: Cilium Assembly |
| [[AGPS]] | -0.52 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[TRAK1]] | -0.49 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[WDR77]] | -0.49 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[LINC02474]] | -0.49 | -0.52 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM58]] | B | TRIM58 activity raises NPHP3's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 1.35× lower at baseline in the lines without TRIM58 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20 |
| [[DNAAF9]] | B | DNAAF9 activity raises NPHP3's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 1.51× lower at baseline in the lines without DNAAF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-26.4, -32.1); signed map (-15.1, 3.2). **Vector** length 112, 32.5% of its response variance represented; |z| ≥ 3 in 1,193 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +6.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.9 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +5.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.6 | +1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | +1.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +2.8 | +2.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.8 | -11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -5.6 | -11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -5.0 | -10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.9 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -4.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | nephrocystin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:132,680,609-132,722,432 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NPH3, KIAA2000, FLJ30691, FLJ36696, MKS7, SLSN3, CFAP31 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Cilia and flagella associated; Inversin complex subunits |
| Reactome | 5 pathways, smallest: Trafficking of myristoylated proteins to the cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z494](https://www.uniprot.org/uniprotkb/Q7Z494) (Nephrocystin-3):

> Required for normal ciliary development and function. Inhibits disheveled-1-induced canonical Wnt-signaling activity and may also play a role in the control of non-canonical Wnt signaling which regulates planar cell polarity. Probably acts as a molecular switch between different Wnt signaling pathways. Required for proper convergent extension cell movements.

**Summary**, from NCBI Gene [27031](https://www.ncbi.nlm.nih.gov/gene/27031):

> This gene encodes a protein containing a coiled-coil (CC) domain, a tubulin-tyrosine ligase (TTL) domain, and a tetratrico peptide repeat (TPR) domain. The encoded protein interacts with nephrocystin, it is required for normal ciliary development, and it functions in renal tubular development. Mutations in this gene are associated with nephronophthisis type 3, and also with renal-hepatic-pancreatic dysplasia, and Meckel syndrome type 7. Naturally occurring read-through transcripts exist between …

**Accessions** — [HGNC:7907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7907) · Entrez [27031](https://www.ncbi.nlm.nih.gov/gene/27031) · UniProt [Q7Z494](https://www.uniprot.org/uniprotkb/Q7Z494) · Ensembl [ENSG00000113971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113971)

## Data

Gene col 3514: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3514); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3514, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3514]; `tensor/DDL_lfc|DDL_z.npy` [3514]; `embed/gene_vectors.npy` [3514]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3514 or target_col == 3514). Every well: [[NPHP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPHP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
