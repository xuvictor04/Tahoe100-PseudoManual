---
symbol: "ANK2"
type: "gene"
col: 6982
ensembl_id: "ENSG00000145362"
name: "ankyrin 2"
location: "4q25-q26"
module: 63
arm: "+"
pooled_cpm: 92.38
n_lines_expressing: 34
n_dd_up: 42
n_dd_down: 32
n_dd_up_clean: 33
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 36
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# ANK2

*ankyrin 2* — 4q25-q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 3.27× (z +15.9, q 0e+00, up in 29 of 32 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 1.60× (z +8.9, q 2e-16, up in 28 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (22 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.401× (z -17.4, q 0e+00, down in 30 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XPOT]] (+0.59, fdr 1e-05), [[TOM1L1]] (+0.57, fdr 1e-05), [[HSPA9]] (+0.57, fdr 1e-05); moves opposite to [[RIN2]] (-0.52, fdr 2e-05), [[SYNJ1]] (-0.47, fdr 3e-05), [[SP3]] (-0.46, fdr 8e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 36 go from it, the strongest it → [[LONP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6982.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **3.27×** | +15.9 | 0e+00 | 29/32 (A498, PANC-1, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.60×** | +8.9 | 2e-16 | 28/32 (C-33 A, A-172, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.48×** | +7.4 | 2e-11 | 29/32 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.60×** | +6.3 | 4e-08 | 22/32 (C-33 A, SW 900, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +6.2 | 7e-08 | 23/31 (A-172, SW480, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.58×** | +6.2 | 7e-08 | 29/32 (SW48, SNU-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.62×** | +6.1 | 1e-07 | 25/34 (A-172, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.56×** | +6.0 | 2e-07 | 24/32 (C-33 A, NCI-H460, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **2.90×** | +6.0 | 2e-07 | 25/31 (LOX-IMVI, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.78×** | +5.7 | 6e-07 | 26/32 (LOX-IMVI, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | **1.50×** | +5.4 | 3e-06 | 24/32 (C-33 A, NCI-H2030, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.44×** | +4.9 | 5e-05 | 20/31 (LOX-IMVI, C-33 A, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.73×** | +4.8 | 7e-05 | 22/32 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.31×** | +4.7 | 1e-04 | 21/32 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +4.5 | 3e-04 | 20/31 (A-172, SNU-1, …) | all doses, stronger at high dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.39×** | +4.4 | 3e-04 | 20/31 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.17×** | +4.3 | 5e-04 | 24/31 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.14×** | +4.3 | 6e-04 | 18/32 (A498, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.57×** | +4.0 | 0.002 | 17/33 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 22 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6982.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.401×** | -17.4 | 0e+00 | 30/33 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.431×** | -16.0 | 0e+00 | 25/32 (LOX-IMVI, C32, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.402×** | -11.8 | 8e-30 | 31/31 (MIA PaCa-2, H4, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.426×** | -11.5 | 2e-28 | 25/32 (MIA PaCa-2, C-33 A, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.466×** | -10.3 | 8e-23 | 28/31 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.469×** | -9.8 | 9e-21 | 24/34 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.487×** | -9.3 | 1e-18 | 24/30 (NCI-H23, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.489×** | -9.3 | 1e-18 | 28/31 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.527×** | -8.6 | 4e-16 | 28/32 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.521×** | -8.4 | 2e-15 | 22/32 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.511×** | -8.4 | 3e-15 | 27/31 (MIA PaCa-2, SNU-1, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.552×** | -8.0 | 6e-14 | 26/32 (RKO, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.593×** | -7.1 | 7e-11 | 23/32 (PANC-1, RKO, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.340×** | -6.1 | 6e-08 | 26/33 (RKO, NCI-H1792, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.651×** | -5.8 | 3e-07 | 22/31 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.372×** | -5.6 | 1e-06 | 24/32 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.765×** | -5.1 | 1e-05 | 19/32 (SNU-423, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.722×** | -4.4 | 3e-04 | 18/32 (SW480, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.738×** | -4.1 | 9e-04 | 16/32 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.740×** | -4.1 | 0.001 | 20/32 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.730×** | -3.9 | 0.002 | 18/31 (SNU-1, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.764×** | -3.6 | 0.005 | 17/33 (RKO, SW48, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.855× | -3.0 | 0.046 | 11/33 (SW480, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6982. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 188 | 2 (1 ⚠) | 16 (11 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.42× (z +13.4) ⚠ unreliable plate only · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.18× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -23.9) |
| [[RKO (line)]] | wt | 417 | 0 | 16 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -22.6) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -20.7) |
| [[SNU-1 (line)]] | wt | 339 | 3 (2 ⚠) | 12 (10 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.07× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -15.5) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 120 | 1 (1 ⚠) | 11 (8 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.41× (z +11.6) ⚠ unreliable plate only | [[Harringtonine (drug)]] 0.5 µM 0.229× (z -14.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -11.2) |
| [[PANC-1 (line)]] | alt | 51.6 | 1 (1 ⚠) | 11 (8 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.23× (z +13.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -21.0) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -15.8) |
| [[SW480 (line)]] | alt | 124 | 0 | 12 (8 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.191× (z -18.1) |
| [[C32 (line)]] | wt | 419 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -25.0) |
| [[NCI-H1792 (line)]] | alt | 193 | 1 (1 ⚠) | 9 (8 ⚠) | [[Selinexor (drug)]] 5 µM 2.31× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -18.8) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -17.8) |
| [[C-33 A (line)]] | alt | 173 | 2 (1 ⚠) | 6 (5 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.95× (z +10.5) ⚠ unreliable plate only · without an alert: [[Neratinib (maleate) (drug)]] 5 µM 2.46× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -10.9) |
| [[H4 (line)]] | wt | 261 | 1 (1 ⚠) | 7 (5 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.32× (z +11.1) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -16.2) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -16.2) |
| [[LOX-IMVI (line)]] | wt | 106 | 2 (1 ⚠) | 6 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.94× (z +12.7) ⚠ unreliable plate only · without an alert: [[5-Azacytidine (drug)]] 5 µM 2.73× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -24.5) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -11.9) |
| [[SW48 (line)]] | wt | 177 | 1 (1 ⚠) | 7 (6 ⚠) | [[Artesunate (drug)]] 5 µM 2.36× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 123 | 2 (2 ⚠) | 5 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.95× (z +11.1) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.115× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -13.8) |
| [[CHP-212 (line)]] | wt | 227 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 110 | 1 (1 ⚠) | 4 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.10× (z +9.7) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -18.4) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -13.0) |
| [[A498 (line)]] | wt | 91.0 | 1 (1 ⚠) | 3 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.60× (z +15.3) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -14.9) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -9.8) |
| [[A-172 (line)]] | wt | 190 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 171 | 1 (1 ⚠) | 2 (1 ⚠) | [[Artesunate (drug)]] 5 µM 2.17× (z +9.3) ⚠ cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -12.4) |
| [[SHP-77 (line)]] | alt | 143 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -9.8) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -9.0) |
| [[AN3 CA (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -12.1) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -11.0) |
| [[J82 (line)]] | alt | 56.7 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.27× (z +9.8) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.7) |
| [[SNU-423 (line)]] | alt | 65.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -13.8) |
| [[A-427 (line)]] | wt | 187 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[HCT15 (line)]] | alt | 61.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -8.6) ⚠ cell-cycle shift, explains ~76% of this change |
| [[HS-578T (line)]] | alt | 29.1 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.27× (z +9.0) ⚠ unreliable plate only | — |
| [[LoVo (line)]] | wt | 24.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.83× (z +10.4) ⚠ unreliable plate only | — |
| [[NCI-H2030 (line)]] | alt | 51.8 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 6.31× (z +12.8) ⚠ unreliable plate only | — |
| [[NCI-H661 (line)]] | alt | 569 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -14.9) |
| [[SK-MEL-2 (line)]] | alt | 177 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[A549 (line)]] | wt | 20.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.94 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.1 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 88.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6982), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPOT]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TOM1L1]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[HSPA9]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[DTD1]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[AARS1]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[TMEM268]] | +0.57 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[GARS1]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PHGDH]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CLGN]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[LINC00662]] | +0.56 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[YARS1]] | +0.56 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[TCEA1]] | +0.55 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIN2]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[SYNJ1]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[SP3]] | -0.46 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[CAB39]] | -0.45 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[EIF4EBP2]] | -0.45 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[CYTH2]] | -0.42 | -0.30 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers ANK2's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.7% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises ANK2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSAT1]] | B | PSAT1 activity raises ANK2's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 3.30× lower at baseline in the lines without PSAT1 | 0.055 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[RIN2]] | B | RIN2 activity lowers ANK2's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 2.82× higher at baseline in the lines without RIN2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[SNCA]] | B | SNCA activity raises ANK2's level | lines that do not express SNCA (29) vs lines expressing it (21) | 2.82× lower at baseline in the lines without SNCA | 0.062 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10 |
| [[ASNSP1]] | B | ASNSP1 activity raises ANK2's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 2.14× lower at baseline in the lines without ASNSP1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[FAM78B]] | B | FAM78B activity raises ANK2's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 2.54× lower at baseline in the lines without FAM78B | 0.096 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[CCNYL2-1]] | C | CCNYL2-1 activity raises ANK2's level | lines that do not express CCNYL2-1 (29) vs lines expressing it (21) | 2.73× lower at baseline in the lines without CCNYL2-1 | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 35, C 1. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LONP1]] | B | ANK2 activity raises LONP1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.58× lower at baseline in the lines without ANK2 | 0.001 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[ACBD6]] | B | ANK2 activity raises ACBD6's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.39× lower at baseline in the lines without ANK2 | 0.007 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[FAM78B]] | B | ANK2 activity raises FAM78B's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 3.24× lower at baseline in the lines without ANK2 | 0.007 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[YARS1]] | B | ANK2 activity raises YARS1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without ANK2 | 0.008 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[SGTB]] | B | ANK2 activity raises SGTB's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without ANK2 | 0.009 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[FOXO3B]] | B | ANK2 activity raises FOXO3B's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 2.00× lower at baseline in the lines without ANK2 | 0.015 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[HSPA9]] | B | ANK2 activity raises HSPA9's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.24× lower at baseline in the lines without ANK2 | 0.015 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[ATP6V1E2]] | B | ANK2 activity raises ATP6V1E2's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.97× lower at baseline in the lines without ANK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[PHGDH]] | B | ANK2 activity raises PHGDH's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 2.17× lower at baseline in the lines without ANK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[RIN2]] | B | ANK2 activity lowers RIN2's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 2.79× higher at baseline in the lines without ANK2 | 0.023 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[UBE3D]] | B | ANK2 activity raises UBE3D's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.52× lower at baseline in the lines without ANK2 | 0.025 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[XPOT]] | B | ANK2 activity raises XPOT's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.34× lower at baseline in the lines without ANK2 | 0.026 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.5, 46.4); signed map (-11.7, 24.5). **Vector** length 130, 42.9% of its response variance represented; |z| ≥ 3 in 1,336 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.51 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.51 to 9); *unfolded protein response* (hallmark, mean cos +0.50 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +11.8 | +15.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +7.6 | +6.0 |
|  | [[EX229 (drug)]] 5 µM |  | +6.7 | +5.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +6.5 | +4.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +6.4 | +4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +6.1 | +4.3 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | -4.4 | -5.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -3.1 | -7.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.7 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -5.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25-q26 — chr4:112,818,032-113,384,221 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAP87, CFAP87; previously LQT4 |
| Gene groups (HGNC) | Cilia and flagella associated; MicroRNA protein coding host genes; ZU5 domain containing ; Ankyrin family |
| Reactome | 10 pathways, smallest: Interaction between L1 and Ankyrins; COPI-mediated anterograde transport; L1CAM interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01484](https://www.uniprot.org/uniprotkb/Q01484) (Ankyrin-2):

> Plays an essential role in the localization and membrane stabilization of ion transporters and ion channels in several cell types, including cardiomyocytes, as well as in striated muscle cells. In skeletal muscle, required for proper localization of DMD and DCTN4 and for the formation and/or stability of a special subset of microtubules associated with costameres and neuromuscular junctions. In cardiomyocytes, required for coordinate assembly of Na/Ca exchanger, SLC8A1/NCX1, Na/K ATPases ATP1A1 …

**Summary**, from NCBI Gene [287](https://www.ncbi.nlm.nih.gov/gene/287):

> This gene encodes a member of the ankyrin family of proteins that link the integral membrane proteins to the underlying spectrin-actin cytoskeleton. Ankyrins play key roles in activities such as cell motility, activation, proliferation, contact and the maintenance of specialized membrane domains. Most ankyrins are typically composed of three structural domains: an amino-terminal domain containing multiple ankyrin repeats; a central region with a highly conserved spectrin binding domain; and a …

**Accessions** — [HGNC:493](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:493) · Entrez [287](https://www.ncbi.nlm.nih.gov/gene/287) · UniProt [Q01484](https://www.uniprot.org/uniprotkb/Q01484) · Ensembl [ENSG00000145362](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145362)

## Data

Gene col 6982: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6982); `tables/drug_effects.parquet` (80 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6982, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6982]; `tensor/DDL_lfc|DDL_z.npy` [6982]; `embed/gene_vectors.npy` [6982]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6982 or target_col == 6982). Every well: [[ANK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
