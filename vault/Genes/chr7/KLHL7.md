---
symbol: "KLHL7"
type: "gene"
col: 4350
ensembl_id: "ENSG00000122550"
name: "kelch like family member 7"
location: "7p15.3"
module: 3
arm: "+"
pooled_cpm: 58.47
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# KLHL7

*kelch like family member 7* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.45× (z +22.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.557× (z -13.8, q 8e-41, down in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.633× (z -11.7, q 3e-29, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH7]] (+0.75, fdr 7e-06), [[CBFA2T2]] (+0.74, fdr 7e-06), [[LMBR1L]] (+0.74, fdr 7e-06); moves opposite to [[TRIM44]] (-0.74, fdr 7e-06), [[HNRNPL]] (-0.69, fdr 2e-05), [[LEKR1]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4350.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.45×** | +22.9 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.27×** | +20.9 | 0e+00 | 46/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.15×** | +19.5 | 0e+00 | 47/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +11.7 | 3e-29 | 35/48 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +11.5 | 2e-28 | 32/49 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +10.6 | 2e-24 | 39/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +9.4 | 4e-19 | 32/49 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +8.8 | 1e-16 | 39/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +7.7 | 1e-12 | 36/49 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.19× | +6.3 | 2e-08 | 22/48 (A498, SNU-423, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.25×** | +5.7 | 6e-07 | 26/48 (H4, HS-578T, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +5.0 | 3e-05 | 19/49 (HT-29, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.21×** | +4.6 | 2e-04 | 22/47 (A498, LS 180, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.41×** | +4.6 | 2e-04 | 17/48 (SW1417, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.18× | +4.2 | 9e-04 | 15/48 (A498, SW1417, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +3.6 | 0.010 | 13/48 (RKO, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.072 | 10/48 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4350.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.557×** | -13.8 | 8e-41 | 34/44 (HS-578T, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.714×** | -12.2 | 1e-31 | 32/48 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.633×** | -11.7 | 3e-29 | 36/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.627×** | -11.5 | 3e-28 | 30/41 (Panc 03.27, KATO III, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.648×** | -11.1 | 1e-26 | 35/49 (NCI-H23, H4, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.664×** | -10.0 | 9e-22 | 31/48 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -8.8 | 1e-16 | 35/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.713×** | -8.6 | 4e-16 | 34/48 (SW480, SNU-423, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.759×** | -7.1 | 1e-10 | 28/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.762×** | -6.9 | 2e-10 | 31/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.762×** | -6.9 | 2e-10 | 26/48 (NCI-H460, KATO III, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.773×** | -6.6 | 2e-09 | 27/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.850× | -5.9 | 2e-07 | 23/48 (hTERT-HPNE, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.804×** | -5.4 | 3e-06 | 22/47 (SNU-423, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.820×** | -5.1 | 1e-05 | 24/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.843× | -4.2 | 8e-04 | 21/48 (LoVo, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.848× | -3.9 | 0.003 | 19/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Docetaxel (drug)]] 5 µM |  | 0.905× | -3.6 | 0.008 | 5/48 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.775×** | -3.4 | 0.017 | 19/48 (NCI-H460, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.780×** | -3.3 | 0.022 | 13/48 (MIA PaCa-2, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4350. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 59.3 | 6 | 8 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.05× (z +15.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -19.3) |
| [[A-172 (line)]] | wt | 102 | 2 | 8 (5 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.03× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -26.3) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -19.6) |
| [[A498 (line)]] | wt | 63.2 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.471× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 61.6 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.01× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -11.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 73.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -14.3) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.373× (z -10.9) |
| [[SW480 (line)]] | alt | 68.6 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.49× (z +15.4) | [[Auranofin (drug)]] 5 µM 0.467× (z -12.8) |
| [[HS-578T (line)]] | alt | 71.4 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.60× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -13.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 66.0 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.49× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.465× (z -8.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 50.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -12.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -9.8) |
| [[H4 (line)]] | wt | 143 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -13.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 59.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.72× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 36.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +10.9) | — |
| [[KATO III (line)]] | alt | 80.4 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.09× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -22.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 50.6 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.436× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 63.8 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 58.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -20.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 40.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 58.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.36× (z +11.6) | [[Lonafarnib (drug)]] 5 µM 0.169× (z -8.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 55.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +10.5) | — |
| [[AsPC-1 (line)]] | alt | 44.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +10.1) | — |
| [[J82 (line)]] | alt | 42.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +12.2) | — |
| [[LoVo (line)]] | wt | 52.3 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.39× (z +10.0) | [[Belumosudil (drug)]] 5 µM 0.465× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 43.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 53.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.47× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 36.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.69× (z +14.0) | — |
| [[NCI-H2347 (line)]] | alt | 54.9 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.43× (z +10.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.484× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 66.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.0895× (z -25.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 75.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -12.7) ⚠ cell-cycle shift, explains ~52% of this change |
| [[hTERT-HPNE (line)]] | wt | 62.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.70× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -9.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 122 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.288× (z -8.6) |
| [[BT-474 (line)]] | alt | 34.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.52× (z +9.4) | — |
| [[C32 (line)]] | wt | 61.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -8.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 58.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 32.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.88× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 61.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.465× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -10.0) |
| [[NCI-H661 (line)]] | alt | 76.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0891× (z -10.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 67.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 44.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 74.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.403× (z -8.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[C-33 A (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4350), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH7]] | +0.75 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.74 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[LMBR1L]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.74 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.74 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[NENF]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.73 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.73 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.72 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[NDUFA2]] | +0.72 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[MACO1]] | +0.71 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM44]] | -0.74 | -0.60 / -0.72 | both halves | 7e-06 |  |
| [[HNRNPL]] | -0.69 | -0.47 / -0.71 | both halves | 2e-05 |  |
| [[LEKR1]] | -0.68 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.68 | -0.74 / -0.63 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.67 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[COA7]] | -0.67 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.67 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[HNRNPU]] | -0.66 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[THOC6]] | -0.66 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[HNRNPA2B1]] | -0.66 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[TASOR]] | -0.65 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.65 | -0.61 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KLHL7's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.778). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.7, -15.4); signed map (-33.9, 13.1). **Vector** length 111, 32.2% of its response variance represented; |z| ≥ 3 in 1,194 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.5 | +19.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.7 | +8.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +3.5 | +6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +20.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.1 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +1.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.4 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.8 | -11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -9.6 | -12.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.5 | -8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.5 | -13.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.9 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -6.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.2 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:23,105,758-23,177,914 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KLHL6, SBBI26, RP42 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXQ5](https://www.uniprot.org/uniprotkb/Q8IXQ5) (Kelch-like protein 7):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin ligase complex. The BCR(KLHL7) complex acts by mediating ubiquitination and subsequent degradation of substrate proteins. Probably mediates 'Lys-48'-linked ubiquitination.

**Summary**, from NCBI Gene [55975](https://www.ncbi.nlm.nih.gov/gene/55975):

> This gene encodes a BTB-Kelch-related protein. The encoded protein may be involved in protein degradation. Mutations in this gene have been associated with retinitis pigmentosa 42. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:15646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15646) · Entrez [55975](https://www.ncbi.nlm.nih.gov/gene/55975) · UniProt [Q8IXQ5](https://www.uniprot.org/uniprotkb/Q8IXQ5) · Ensembl [ENSG00000122550](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122550)

## Data

Gene col 4350: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4350); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4350, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4350]; `tensor/DDL_lfc|DDL_z.npy` [4350]; `embed/gene_vectors.npy` [4350]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4350 or target_col == 4350). Every well: [[KLHL7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
