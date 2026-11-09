---
symbol: "PCLAF"
type: "gene"
col: 9361
ensembl_id: "ENSG00000166803"
name: "PCNA clamp associated factor"
location: "15q22.31"
module: 6
arm: "+"
pooled_cpm: 25.51
n_lines_expressing: 48
n_dd_up: 28
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# PCLAF

*PCNA clamp associated factor* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.30× (z +17.3, q 0e+00, up in 39 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.40× (z +4.9, q 3e-05, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.504× (z -10.1, q 4e-21, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD54L]] (+0.90, fdr 7e-06), [[EXO1]] (+0.88, fdr 7e-06), [[RAD51AP1]] (+0.88, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9361.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **5.30×** | +17.3 | 0e+00 | 39/39 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **4.92×** | +15.9 | 0e+00 | 35/35 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **3.44×** | +11.9 | 3e-30 | 34/36 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.02×** | +10.3 | 1e-22 | 33/45 (A549, NCI-H2347, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.92×** | +6.5 | 7e-09 | 36/45 (SW480, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.78×** | +6.0 | 2e-07 | 31/46 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.78×** | +5.8 | 7e-07 | 34/46 (SW480, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.74×** | +5.7 | 7e-07 | 32/45 (A498, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.67×** | +5.3 | 6e-06 | 28/46 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~81% of this change | **1.68×** | +5.2 | 1e-05 | 32/44 (C32, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.62×** | +5.0 | 3e-05 | 24/44 (Panc 03.27, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.40×** | +5.0 | 3e-05 | 26/46 (HT-29, SW48, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.9 | 3e-05 | 27/46 (SW480, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~78% of this change | **1.63×** | +4.9 | 4e-05 | 22/42 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.62×** | +4.8 | 6e-05 | 31/45 (PANC-1, A-427, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.46×** | +3.9 | 0.003 | 22/46 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.025 | 16/45 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.030 | 15/45 (A-172, A498, …) | top dose only | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.031 | 19/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.055 | 16/45 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.32×** | +2.9 | 0.075 | 10/46 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Aliskiren (drug)]] 5 µM |  | **1.21×** | +2.8 | 0.095 | 8/46 (SW480, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9361.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.504×** | -10.1 | 4e-21 | 36/46 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.395×** | -9.7 | 1e-19 | 34/45 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.526×** | -6.7 | 5e-09 | 28/46 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.476×** | -5.5 | 5e-06 | 29/46 (LoVo, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.705×** | -5.1 | 3e-05 | 30/46 (HCT15, Hs 766T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.751×** | -4.2 | 0.002 | 22/46 (LoVo, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.663×** | -4.1 | 0.003 | 19/46 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.655×** | -3.7 | 0.018 | 24/46 (LS 180, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.658×** | -3.6 | 0.019 | 19/46 (LoVo, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.722×** | -3.4 | 0.039 | 21/45 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.540×** | -3.3 | 0.042 | 15/45 (A-427, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.560×** | -3.2 | 0.071 | 15/46 (LS 180, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.807×** | -3.1 | 0.071 | 19/46 (RKO, SW 1088, …) | all doses, flat |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.659×** | -3.1 | 0.079 | 16/46 (LoVo, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.814×** | -3.0 | 0.087 | 18/46 (SHP-77, RKO, …) | top dose only | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.576×** | -3.0 | 0.091 | 16/45 (A-427, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.32 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9361. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.7 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.46× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -11.4) |
| [[LoVo (line)]] | wt | 28.1 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | [[Selinexor (drug)]] 5 µM 0.188× (z -14.8) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.209× (z -13.8) |
| [[LS 180 (line)]] | wt | 24.7 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -16.1) |
| [[SW480 (line)]] | alt | 29.3 | 3 (3 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.5) ⚠ cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -12.9) |
| [[A498 (line)]] | wt | 22.4 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | [[Selinexor (drug)]] 5 µM 0.229× (z -13.8) ⚠ cell-cycle shift, explains ~99% of this change |
| [[HOP62 (line)]] | alt | 23.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -10.1) |
| [[HT-29 (line)]] | alt | 31.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.31× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -9.7) |
| [[KATO III (line)]] | alt | 38.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.41× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 21.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 8.80× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.0951× (z -11.8) |
| [[PANC-1 (line)]] | alt | 33.8 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.44× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[A-427 (line)]] | wt | 31.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0985× (z -14.1) |
| [[A549 (line)]] | wt | 29.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.12× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[HEC-1-A (line)]] | alt | 38.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -14.2) |
| [[Hs 766T (line)]] | wt | 17.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.93× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0997× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 26.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.33× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -10.5) |
| [[A-172 (line)]] | wt | 29.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.13× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[H4 (line)]] | wt | 25.9 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0353× (z -13.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.166× (z -10.5) |
| [[HS-578T (line)]] | alt | 10.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.58× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[J82 (line)]] | alt | 44.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[LOX-IMVI (line)]] | wt | 20.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.0× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.33× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 26.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 30.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[HCT15 (line)]] | alt | 44.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 25.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +11.3) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[RKO (line)]] | wt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.4) |
| [[SHP-77 (line)]] | alt | 33.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.66× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0989× (z -9.9) |
| [[SNU-1 (line)]] | wt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -11.2) |
| [[SNU-423 (line)]] | alt | 17.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.66× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[SW 900 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.63× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[SW1417 (line)]] | alt | 23.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[AN3 CA (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9361), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD54L]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | STRING 595 |
| [[EXO1]] | +0.88 | +0.89 / +0.87 | both halves | 7e-06 | STRING 652 |
| [[RAD51AP1]] | +0.88 | +0.85 / +0.89 | both halves | 7e-06 | STRING 516 |
| [[FANCI]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 | STRING 518 |
| [[MYBL2]] | +0.87 | +0.87 / +0.87 | both halves | 7e-06 |  |
| [[WDR76]] | +0.87 | +0.86 / +0.86 | both halves | 7e-06 |  |
| [[TK1]] | +0.86 | +0.83 / +0.86 | both halves | 7e-06 | STRING 820 |
| [[DSCC1]] | +0.85 | +0.83 / +0.85 | both halves | 7e-06 |  |
| [[SPC25]] | +0.85 | +0.83 / +0.85 | both halves | 7e-06 | STRING 705 |
| [[CENPK]] | +0.84 | +0.85 / +0.84 | both halves | 7e-06 | STRING 536 |
| [[CLSPN]] | +0.84 | +0.80 / +0.85 | both halves | 7e-06 |  |
| [[DTL]] | +0.84 | +0.85 / +0.82 | both halves | 7e-06 | pathway: DNA Damage Bypass; STRING 794 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises PCLAF's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.52× lower at baseline in the lines without TCF19 | 0.002 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PCLAF's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.9% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[E2F8]] | B | E2F8 activity raises PCLAF's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.17× lower at baseline in the lines without E2F8 | 0.021 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises PCLAF's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.71× lower at baseline in the lines without MCM10 | 0.004 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises PCLAF's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.69× lower at baseline in the lines without PBK | 0.004 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[MELK]], [[TK1]] | C | MELK, TK1 activity raises PCLAF's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 3.56× lower at baseline in the lines without MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[MYBL2]] | C | MYBL2 activity raises PCLAF's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.87× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises PCLAF's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.82× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[PKMYT1]] | C | PKMYT1 activity raises PCLAF's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.76× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; its own permutation p |
| [[C21orf58]], [[CDC45]], [[CENPM]] | C | C21orf58, CDC45, CENPM activity raises PCLAF's level | lines that do not express C21orf58, CDC45, CENPM (3) vs lines expressing them (47) | 2.70× lower at baseline in the lines without C21orf58, CDC45, CENPM | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CLSPN]] | C | CLSPN activity raises PCLAF's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without CLSPN | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.888). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.7, -45.1); signed map (-38.0, -44.3). **Vector** length 120, 40.0% of its response variance represented; |z| ≥ 3 in 1,198 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.66 to 65); *DNA strand elongation* (reactome, mean cos +0.70 to 28); *DNA Replication* (reactome, mean cos +0.69 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +5.3 | +5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +5.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +4.2 | +17.3 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +4.2 | +5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.9 | +10.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +1.9 |
|  | [[Methotrexate (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.4 | +0.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.3 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.6 | -10.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | -5.5 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -4.8 | -6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.5 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | PCNA clamp associated factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:64,364,304-64,387,687 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NS5ATP9, OEATC-1, p15(PAF), PAF15; previously KIAA0101 |
| Reactome | 4 pathways, smallest: Termination of translesion DNA synthesis; Translesion synthesis by Y family DNA polymerases bypasses lesions on DNA template; DNA Damage Bypass |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15004](https://www.uniprot.org/uniprotkb/Q15004) (PCNA-associated factor):

> PCNA-binding protein that acts as a regulator of DNA repair during DNA replication. Following DNA damage, the interaction with PCNA is disrupted, facilitating the interaction between monoubiquitinated PCNA and the translesion DNA synthesis DNA polymerase eta (POLH) at stalled replisomes, facilitating the bypass of replication-fork-blocking lesions. Also acts as a regulator of centrosome number.

**Summary**, from NCBI Gene [9768](https://www.ncbi.nlm.nih.gov/gene/9768):

> Enables chromatin binding activity and molecular adaptor activity. Involved in several processes, including centrosome cycle; response to UV; and translesion synthesis. Located in centrosome; nucleus; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28961) · Entrez [9768](https://www.ncbi.nlm.nih.gov/gene/9768) · UniProt [Q15004](https://www.uniprot.org/uniprotkb/Q15004) · Ensembl [ENSG00000166803](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166803)

## Data

Gene col 9361: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9361); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9361, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9361]; `tensor/DDL_lfc|DDL_z.npy` [9361]; `embed/gene_vectors.npy` [9361]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9361 or target_col == 9361). Every well: [[PCLAF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCLAF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
