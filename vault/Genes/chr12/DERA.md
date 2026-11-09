---
symbol: "DERA"
type: "gene"
col: 349
ensembl_id: "ENSG00000023697"
name: "deoxyribose-phosphate aldolase"
location: "12p12.3"
module: 29
arm: "+"
pooled_cpm: 59.87
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 12
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# DERA

*deoxyribose-phosphate aldolase* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +12.8, q 2e-34, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.581× (z -9.4, q 5e-18, down in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.661× (z -7.4, q 4e-11, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANXA4]] (+0.64, fdr 3e-05), [[STRADB]] (+0.62, fdr 1e-05), [[RAB11FIP2]] (+0.61, fdr 3e-05); moves opposite to [[SPATA2L]] (-0.63, fdr 3e-05), [[GGA1]] (-0.62, fdr 4e-05), [[CLIP2]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 349.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +12.8 | 2e-34 | 40/49 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +12.5 | 3e-33 | 40/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +10.4 | 4e-23 | 40/49 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +9.5 | 5e-19 | 31/45 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.40×** | +6.5 | 1e-08 | 33/49 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +6.4 | 2e-08 | 25/37 (LOX-IMVI, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +6.3 | 3e-08 | 33/47 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.41×** | +6.2 | 5e-08 | 28/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.28×** | +6.0 | 1e-07 | 26/48 (A498, J82, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.38×** | +5.7 | 7e-07 | 30/47 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +5.3 | 5e-06 | 24/47 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +5.3 | 6e-06 | 23/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.33×** | +4.9 | 3e-05 | 25/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.34×** | +4.9 | 5e-05 | 27/48 (NCI-H460, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +4.9 | 5e-05 | 29/49 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +4.7 | 9e-05 | 23/48 (C32, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 4e-04 | 21/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 8e-04 | 24/47 (Hs 766T, NCI-H1573, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.9 | 0.003 | 20/48 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.003 | 21/49 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.010 | 17/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 349.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.581×** | -9.4 | 5e-18 | 40/48 (NCI-H460, LS 180, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.661×** | -7.4 | 4e-11 | 34/47 (HepG2/C3A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.716×** | -6.0 | 4e-07 | 26/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.719×** | -5.9 | 5e-07 | 26/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **0.734×** | -5.3 | 1e-05 | 26/47 (H4, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.750×** | -5.1 | 2e-05 | 25/47 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.721×** | -4.2 | 0.002 | 24/47 (C32, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.814×** | -3.7 | 0.015 | 23/48 (LS 180, SW48, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.816×** | -3.7 | 0.016 | 20/48 (LoVo, SW48, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.689×** | -3.5 | 0.027 | 20/48 (Hs 766T, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.765×** | -3.4 | 0.032 | 18/48 (H4, CFPAC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.831×** | -3.2 | 0.067 | 16/43 (LoVo, SHP-77, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.1 | 0.073 | 23/48 (LS 180, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 349. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 170 | 1 (1 ⚠) | 10 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.30× (z +9.7) ⚠ cell-cycle shift, explains ~28% of this change | [[Harringtonine (drug)]] 5 µM 0.155× (z -14.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.215× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 47.6 | 8 (4 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 5.77× (z +18.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +16.4) | [[Harringtonine (drug)]] 5 µM 0.249× (z -15.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 46.6 | 8 (4 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +16.0) | — |
| [[A549 (line)]] | wt | 54.4 | 2 (1 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -15.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 34.8 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +11.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 82.9 | 4 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +11.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.421× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 46.5 | 4 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +10.7) | — |
| [[RKO (line)]] | wt | 73.1 | 2 (2 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 2.60× (z +8.8) ⚠ cell-cycle shift, explains ~28% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.206× (z -14.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 412 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -9.5) |
| [[A-172 (line)]] | wt | 29.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 2.56× (z +8.7) | — |
| [[H4 (line)]] | wt | 37.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 8.40× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +10.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0980× (z -12.3) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[LoVo (line)]] | wt | 122 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW480 (line)]] | alt | 74.8 | 1 | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.504× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.513× (z -8.6) |
| [[COLO 205 (line)]] | alt | 74.7 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.279× (z -9.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 21.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +10.0) | — |
| [[J82 (line)]] | alt | 42.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.10× (z +9.1) ⚠ cell-cycle shift, explains ~59% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.280× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[NCI-H1792 (line)]] | alt | 73.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.77× (z +9.1) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.317× (z -10.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 99.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 43.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[ULK-101 (drug)]] 5 µM 0.104× (z -9.3) |
| [[SW 900 (line)]] | alt | 41.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.93× (z +10.9) | — |
| [[SW48 (line)]] | wt | 65.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 91.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.406× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[AN3 CA (line)]] | alt | 72.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 31.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.80× (z +19.1) | — |
| [[C32 (line)]] | wt | 63.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.317× (z -9.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[CFPAC-1 (line)]] | alt | 53.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 50.0 | 0 | 1 | — | [[4EGI-1 (drug)]] 5 µM 0.0884× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 34.5 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.106× (z -14.1) |
| [[HT-29 (line)]] | alt | 51.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.52× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 68.9 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 91.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.456× (z -8.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[BT-474 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 72.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 349), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA4]] | +0.64 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[STRADB]] | +0.62 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[RAB11FIP2]] | +0.61 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[CIAO2A]] | +0.59 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[EI24]] | +0.59 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[DECR1]] | +0.58 | +0.56 / +0.35 | both halves | 1e-04 |  |
| [[NNT]] | +0.57 | +0.56 / +0.35 | both halves | 1e-04 |  |
| [[MDM2]] | +0.57 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[ACTA2]] | +0.57 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[FAS]] | +0.57 | +0.51 / +0.36 | both halves | 9e-05 |  |
| [[AK3]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[TMEM68]] | +0.56 | +0.45 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA2L]] | -0.63 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[GGA1]] | -0.62 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[CLIP2]] | -0.61 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[STX1A]] | -0.59 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[ASMTL]] | -0.59 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[PILRB]] | -0.59 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[TNFAIP8L1]] | -0.58 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[BMERB1]] | -0.56 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[TBC1D10A]] | -0.55 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[DLGAP4]] | -0.55 | -0.50 / -0.42 | both halves | 4e-05 | STRING 421 |
| [[PLIN3]] | -0.55 | -0.59 / -0.36 | both halves | 9e-05 |  |
| [[KCTD20]] | -0.55 | -0.50 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DERA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02057]] | B | LINC02057 activity lowers DERA's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 1.55× higher at baseline in the lines without LINC02057 | 0.043 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[TOP1]] | B | TOP1 activity lowers DERA's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TLCD4]], [[TLCD4-RWDD3]] | B | TLCD4, TLCD4-RWDD3 activity raises DERA's level | lines that do not express TLCD4, TLCD4-RWDD3 (11) vs lines expressing them (39) | 1.55× lower at baseline in the lines without TLCD4, TLCD4-RWDD3 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent; co-absent genes |
| [[MAP2K1]] | B | MAP2K1 activity lowers DERA's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GCDH]] | C | GCDH's natural level weakens DERA's drug response | GCDH's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.01; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TP53]] | C | TP53 activity strengthens DERA's drug response | recorded loss-of-function mutation of TP53 in 32 lines vs 17 not recorded | the TP53-altered lines respond 0.65× as strongly (z diff +1.47); strongest at Idarubicin (hydrochloride) 0.5 µM: 1.27x vs 2.09x (z diff +3.2) | 0.471 over the table, 0.023 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.518). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-12.0, 14.0); signed map (37.7, -23.5). **Vector** length 127, 37.1% of its response variance represented; |z| ≥ 3 in 1,438 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +12.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +10.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +7.5 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.7 | +3.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +4.6 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.1 | +4.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.7 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -6.5 | -9.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.4 | -6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.3 | -5.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -3.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.7 | -3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -4.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | deoxyribose-phosphate aldolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.3 — chr12:15,911,302-16,037,381 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-26, DEOC |
| Gene groups (HGNC) | Aldehyde lyases |
| Reactome | 4 pathways, smallest: Pentose phosphate pathway; Metabolism of carbohydrates and carbohydrate derivatives; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y315](https://www.uniprot.org/uniprotkb/Q9Y315) (Deoxyribose-phosphate aldolase):

> Catalyzes a reversible aldol reaction between acetaldehyde and D-glyceraldehyde 3-phosphate to generate 2-deoxy-D-ribose 5-phosphate. Participates in stress granule (SG) assembly. May allow ATP production from extracellular deoxyinosine in conditions of energy deprivation.

**Summary**, from NCBI Gene [51071](https://www.ncbi.nlm.nih.gov/gene/51071):

> Enables deoxyribose-phosphate aldolase activity. Involved in 2'-deoxyribonucleoside catabolic process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24269](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24269) · Entrez [51071](https://www.ncbi.nlm.nih.gov/gene/51071) · UniProt [Q9Y315](https://www.uniprot.org/uniprotkb/Q9Y315) · Ensembl [ENSG00000023697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023697)

## Data

Gene col 349: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 349); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 349, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 349]; `tensor/DDL_lfc|DDL_z.npy` [349]; `embed/gene_vectors.npy` [349]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 349 or target_col == 349). Every well: [[DERA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DERA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
