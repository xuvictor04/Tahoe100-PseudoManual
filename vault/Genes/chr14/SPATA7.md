---
symbol: "SPATA7"
type: "gene"
col: 484
ensembl_id: "ENSG00000042317"
name: "spermatogenesis associated 7"
location: "14q31.3"
module: 178
arm: "+"
pooled_cpm: 29.47
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 31
n_dd_up_clean: 13
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# SPATA7

*spermatogenesis associated 7* — 14q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.61× (z +8.7, q 2e-15, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.399× (z -16.1, q 0e+00, down in 32 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.458× (z -14.2, q 1e-43, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX3]] (+0.77, fdr 7e-06), [[CRYZL1]] (+0.72, fdr 7e-06), [[EXOC1]] (+0.71, fdr 7e-06); moves opposite to [[RNF32-AS1]] (-0.73, fdr 7e-06), [[SFPQ]] (-0.66, fdr 1e-05), [[THOC6]] (-0.66, fdr 7e-06).
> It is in [[Module 178]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 484.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +8.7 | 2e-15 | 33/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +8.1 | 2e-13 | 32/48 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.6 | 6e-12 | 25/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +6.9 | 7e-10 | 32/48 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.29×** | +6.6 | 5e-09 | 27/48 (LoVo, SW480, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +6.3 | 2e-08 | 30/48 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.1 | 2e-05 | 23/48 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.59×** | +4.5 | 5e-04 | 21/47 (SW 900, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.27×** | +4.4 | 7e-04 | 21/48 (LS 180, RKO, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +4.4 | 7e-04 | 11/48 (AsPC-1, A-427, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 9e-04 | 17/48 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.001 | 16/48 (KATO III, NCI-H1792, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.003 | 16/48 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.20×** | +4.0 | 0.003 | 14/48 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.006 | 15/48 (SW480, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.011 | 13/48 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.011 | 9/47 (NCI-H460, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 484.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.399×** | -16.1 | 0e+00 | 32/37 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.425×** | -15.0 | 0e+00 | 39/46 (SNU-423, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.458×** | -14.2 | 1e-43 | 42/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.472×** | -13.7 | 2e-40 | 34/45 (CFPAC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.477×** | -13.5 | 2e-39 | 34/47 (HS-578T, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.481×** | -13.4 | 1e-38 | 40/48 (SW480, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.609×** | -12.7 | 3e-35 | 36/48 (NCI-H1792, SK-MEL-2, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.500×** | -12.5 | 8e-34 | 42/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.499×** | -11.7 | 7e-30 | 29/39 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.571×** | -10.2 | 1e-22 | 37/48 (LS 180, SW480, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.580×** | -9.5 | 8e-20 | 32/48 (NCI-H1792, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.596×** | -9.3 | 7e-19 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.616×** | -8.8 | 5e-17 | 34/48 (HCT15, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.466×** | -7.3 | 1e-11 | 25/48 (Panc 03.27, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.667×** | -7.3 | 1e-11 | 31/48 (C32, HCT15, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.479×** | -7.0 | 8e-11 | 27/48 (NCI-H1792, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -7.0 | 1e-10 | 28/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.700×** | -6.5 | 3e-09 | 26/48 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.699×** | -6.1 | 2e-08 | 25/48 (PANC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.833×** | -4.7 | 8e-05 | 21/48 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.838× | -4.5 | 2e-04 | 21/48 (MIA PaCa-2, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.787×** | -4.2 | 7e-04 | 19/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 484. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.1 | 1 | 16 (8 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -17.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.202× (z -16.9) |
| [[HOP62 (line)]] | alt | 36.4 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -20.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.356× (z -13.4) |
| [[SW480 (line)]] | alt | 38.4 | 0 | 11 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -18.6) |
| [[HCT15 (line)]] | alt | 62.2 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.133× (z -13.9) |
| [[LS 180 (line)]] | wt | 45.8 | 1 | 7 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.148× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.156× (z -17.3) |
| [[A549 (line)]] | wt | 36.8 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0965× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.230× (z -12.9) |
| [[LOX-IMVI (line)]] | wt | 24.2 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 64.1 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -27.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[CFPAC-1 (line)]] | alt | 46.5 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.403× (z -8.6) |
| [[PANC-1 (line)]] | alt | 17.9 | 0 | 5 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.230× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 36.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -18.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -9.9) |
| [[SNU-423 (line)]] | alt | 26.5 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -15.3) ⚠ toxic |
| [[C32 (line)]] | wt | 15.2 | 0 | 4 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.137× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 29.4 | 0 | 4 (3 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.121× (z -11.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.304× (z -8.7) |
| [[A-172 (line)]] | wt | 26.4 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.244× (z -11.5) |
| [[Hs 766T (line)]] | wt | 35.8 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 5 µM 0.0517× (z -11.6) |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -14.4) |
| [[J82 (line)]] | alt | 18.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -11.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 58.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -16.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 27.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -14.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H2347 (line)]] | alt | 35.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -10.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 40.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.159× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 33.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0767× (z -25.9) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SNU-1 (line)]] | wt | 29.9 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -11.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -8.7) |
| [[SW 1088 (line)]] | alt | 54.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0469× (z -12.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0572× (z -8.5) |
| [[A-427 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -9.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0969× (z -13.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -12.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 12.5 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0837× (z -9.3) |
| [[KATO III (line)]] | alt | 22.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.262× (z -9.4) |
| [[LoVo (line)]] | wt | 21.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 24.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.289× (z -9.0) |
| [[RKO (line)]] | wt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 35.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -9.4) |
| [[SW1417 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0543× (z -19.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 47.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.5) | — |
| [[A498 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 484), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX3]] | +0.77 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[EXOC1]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.69 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[CNIH4]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[CCS]] | +0.67 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[C12orf76]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.67 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[VDAC3]] | +0.66 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[ZNF654]] | +0.66 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[SNAPC3]] | +0.66 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ASB7]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF32-AS1]] | -0.73 | -0.64 / -0.71 | both halves | 7e-06 |  |
| [[SFPQ]] | -0.66 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[THOC6]] | -0.66 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[HNRNPAB]] | -0.62 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[SSU72]] | -0.61 | -0.41 / -0.68 | both halves | 4e-05 |  |
| [[CFAP161]] | -0.61 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[TBILA]] | -0.61 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[SSUH2]] | -0.61 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[PHEX]] | -0.59 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[TRIM44]] | -0.59 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[LINC00641]] | -0.59 | -0.36 / -0.65 | both halves | 1e-04 |  |
| [[SLC2A9]] | -0.59 | -0.50 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.735). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.3, -12.7); signed map (-33.2, -4.7). **Vector** length 93.0, 24.3% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +4.1 | +6.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +4.4 |
|  | [[NG25 (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +6.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +2.8 | +4.4 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.3 | +2.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +4.2 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +1.9 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.1 | -13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.7 | -16.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.7 | -13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -11.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.6 | -15.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q31.3 — chr14:88,384,924-88,470,350 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSD3; previously LCA3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0W8](https://www.uniprot.org/uniprotkb/Q9P0W8) (Spermatogenesis-associated protein 7):

> Involved in the maintenance of both rod and cone photoreceptor cells (By similarity). It is required for recruitment and proper localization of RPGRIP1 to the photoreceptor connecting cilium (CC), as well as photoreceptor-specific localization of proximal CC proteins at the distal CC (By similarity). Maintenance of protein localization at the photoreceptor-specific distal CC is essential for normal microtubule stability and to prevent photoreceptor degeneration (By similarity).

**Summary**, from NCBI Gene [55812](https://www.ncbi.nlm.nih.gov/gene/55812):

> This gene, originally isolated from testis, is also expressed in retina. Mutations in this gene are associated with Leber congenital amaurosis and juvenile retinitis pigmentosa. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:20423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20423) · Entrez [55812](https://www.ncbi.nlm.nih.gov/gene/55812) · UniProt [Q9P0W8](https://www.uniprot.org/uniprotkb/Q9P0W8) · Ensembl [ENSG00000042317](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000042317)

## Data

Gene col 484: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 484); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 484, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 484]; `tensor/DDL_lfc|DDL_z.npy` [484]; `embed/gene_vectors.npy` [484]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 484 or target_col == 484). Every well: [[SPATA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
