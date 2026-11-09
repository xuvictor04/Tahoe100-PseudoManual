---
symbol: "HNRNPAB"
type: "gene"
col: 12400
ensembl_id: "ENSG00000197451"
name: "heterogeneous nuclear ribonucleoprotein A/B"
location: "5q35.3"
module: 5
arm: "+"
pooled_cpm: 52.15
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# HNRNPAB

*heterogeneous nuclear ribonucleoprotein A/B* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (27 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.78× (z +17.5, q 0e+00, up in 48 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.30× (z +9.3, q 2e-18, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.708× (z -5.5, q 2e-05, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~82% of this change. The strongest without an alert is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 0.798× (z -3.6, q 0.035, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTPS1]] (+0.80, fdr 7e-06), [[SLFNL1-AS1]] (+0.76, fdr 7e-06), [[LETM1]] (+0.71, fdr 7e-06); moves opposite to [[ZCRB1]] (-0.69, fdr 7e-06), [[CFAP36]] (-0.68, fdr 7e-06), [[IFI27L2]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 29 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 27 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **4.78×** | +17.5 | 0e+00 | 48/48 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **4.46×** | +16.1 | 0e+00 | 40/41 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.55×** | +13.1 | 5e-37 | 43/45 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.83×** | +9.5 | 2e-19 | 37/48 (A549, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.30×** | +9.3 | 2e-18 | 43/48 (SNU-423, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.12×** | +8.4 | 4e-15 | 37/47 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **2.16×** | +8.3 | 1e-14 | 41/47 (NCI-H1792, Panc 03.27, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.7 | 1e-12 | 40/48 (SNU-423, CFPAC-1, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.94×** | +7.4 | 7e-12 | 39/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.89×** | +7.1 | 7e-11 | 40/48 (AsPC-1, H4, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.80×** | +6.6 | 3e-09 | 37/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.80×** | +6.3 | 1e-08 | 36/47 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.80×** | +6.3 | 1e-08 | 38/47 (H4, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.48×** | +6.2 | 3e-08 | 31/48 (C32, NCI-H1792, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.74×** | +5.9 | 1e-07 | 36/48 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +5.8 | 3e-07 | 31/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +5.5 | 1e-06 | 30/48 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +5.3 | 4e-06 | 30/48 (PANC-1, CFPAC-1, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.62×** | +5.2 | 5e-06 | 31/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.006 | 23/47 (NCI-H460, HOP62, …) | all doses, flat | position effect removed |
| [[vincristine (drug)]] 5 µM |  | **1.82×** | +3.5 | 0.010 | 23/45 (NCI-H23, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.029 | 21/48 (RKO, A-427, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.64×** | +2.9 | 0.062 | 18/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.64×** | +2.9 | 0.062 | 18/48 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.31×** | +2.9 | 0.065 | 16/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +2.8 | 0.081 | 18/47 (NCI-H460, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.31×** | +2.8 | 0.081 | 19/48 (NCI-H460, SW 900, …) | all doses, flat | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.27×** | +2.7 | 0.100 | 17/48 (BT-474, NCI-H2030, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12400.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.708×** | -5.5 | 2e-05 | 31/48 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.639×** | -5.0 | 1e-04 | 36/48 (LS 180, A-427, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.772×** | -4.1 | 0.007 | 28/48 (HEC-1-A, RKO, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.699×** | -4.0 | 0.008 | 31/48 (Hs 766T, PANC-1, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.798×** | -3.6 | 0.035 | 22/48 (NCI-H2030, SW1417, …) | rises with dose | position effect removed |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.730×** | -3.4 | 0.059 | 24/48 (NCI-H2347, CFPAC-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.576×** | -3.2 | 0.094 | 20/48 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.822× | -3.1 | 0.11 | 17/48 (A-427, SW48, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.734× | -3.1 | 0.11 | 18/48 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.761× | -3.1 | 0.11 | 22/48 (HEC-1-A, COLO 205, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.76 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 18.1 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.9× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 6.41× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 27.2 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +12.8) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.45× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 21.3 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.0× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 7.15× (z +10.0) | — |
| [[A-427 (line)]] | wt | 99.8 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.291× (z -14.2) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -9.7) |
| [[C32 (line)]] | wt | 28.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +13.4) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.43× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 30.2 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.51× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.98× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 41.3 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.03× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.46× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 40.0 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.58× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.24× (z +8.5) | — |
| [[A498 (line)]] | wt | 62.8 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.504× (z -8.8) ⚠ cell-cycle shift, explains ~82% of this change |
| [[A549 (line)]] | wt | 25.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.5× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LOX-IMVI (line)]] | wt | 38.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.40× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 47.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.52× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.08× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 54.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[PANC-1 (line)]] | alt | 44.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW480 (line)]] | alt | 60.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.28× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-172 (line)]] | wt | 33.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[AsPC-1 (line)]] | alt | 34.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +11.3) ⚠ cell-cycle shift, explains ~86% of this change | — |
| [[H4 (line)]] | wt | 44.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.28× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.86× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 29.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.96× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HT-29 (line)]] | alt | 54.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.73× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +11.4) ⚠ cell-cycle shift, explains ~86% of this change | — |
| [[LoVo (line)]] | wt | 67.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.89× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Selinexor (drug)]] 5 µM 0.474× (z -8.5) ⚠ cell-cycle shift, explains ~82% of this change |
| [[LS 180 (line)]] | wt | 108 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.244× (z -14.1) ⚠ cell-cycle shift, explains ~82% of this change |
| [[RPMI-7951 (line)]] | alt | 25.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.58× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[J82 (line)]] | alt | 79.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[KATO III (line)]] | alt | 59.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1573 (line)]] | alt | 22.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.34× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H23 (line)]] | alt | 67.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H2347 (line)]] | alt | 51.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 74.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW 900 (line)]] | alt | 60.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.1) ⚠ cell-cycle shift, explains ~86% of this change | — |
| [[SW1417 (line)]] | alt | 86.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[AN3 CA (line)]] | alt | 87.7 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.199× (z -8.7) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 71.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[COLO 205 (line)]] | alt | 42.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +10.0) ⚠ cell-cycle shift, explains ~86% of this change | — |
| [[HCT15 (line)]] | alt | 50.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.27× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HEC-1-A (line)]] | alt | 72.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HepG2_C3A (line)]] | wt | 33.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[RKO (line)]] | wt | 84.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SNU-1 (line)]] | wt | 44.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[BT-474 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 75.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTPS1]] | +0.80 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[SLFNL1-AS1]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[LETM1]] | +0.71 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[PSME3]] | +0.70 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[WDR4]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[DOCK1]] | +0.67 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[MACROH2A1]] | +0.66 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[UGGT2]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.65 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[ARMC6]] | +0.65 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[TTF2]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[NOLC1]] | +0.64 | +0.64 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCRB1]] | -0.69 | -0.63 / -0.64 | both halves | 7e-06 | same gene group; STRING 421 |
| [[CFAP36]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[IFI27L2]] | -0.68 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[KBTBD3]] | -0.68 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[SNX2]] | -0.67 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[AFTPH]] | -0.67 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[HADHB]] | -0.67 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[OGA]] | -0.66 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[THAP8]] | -0.66 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[VPS37D]] | -0.66 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[EXOC1]] | -0.66 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[SECISBP2L]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises HNRNPAB's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.97× lower at baseline in the lines without CDC25A | 0.029 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[PLXNA2]] | B | PLXNA2 activity lowers HNRNPAB's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.29× higher at baseline in the lines without PLXNA2 | 0.060 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[TOP2A]] | B | TOP2A activity lowers HNRNPAB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CHSY3]] | B | CHSY3 activity lowers HNRNPAB's level | lines that do not express CHSY3 (23) vs lines expressing it (27) | 1.45× higher at baseline in the lines without CHSY3 | 0.079 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, ZNF365, GBP5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.9, -35.1); signed map (2.9, -50.7). **Vector** length 105, 39.8% of its response variance represented; |z| ≥ 3 in 1,331 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.53 to 13); *ribosome biogenesis* (control, mean cos +0.54 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +7.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.1 | +7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.8 | +6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +9.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +1.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.8 | -0.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -8.0 | -5.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -6.4 | -5.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -4.5 | -4.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | -3.6 | -4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.3 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.6 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein A/B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:178,204,533-178,211,163 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ABBP1, FLJ40338; previously HNRPAB |
| Gene groups (HGNC) | RNA binding motif containing; Spliceosomal A complex; Heterogeneous nuclear ribonucleoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99729](https://www.uniprot.org/uniprotkb/Q99729) (Heterogeneous nuclear ribonucleoprotein A/B):

> Binds single-stranded RNA. Has a high affinity for G-rich and U-rich regions of hnRNA. Also binds to APOB mRNA transcripts around the RNA editing site.

**Summary**, from NCBI Gene [3182](https://www.ncbi.nlm.nih.gov/gene/3182):

> This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are produced by RNA polymerase II and are components of the heterogeneous nuclear RNA (hnRNA) complexes. They are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the nucleus, some seem to shuttle between the nucleus and the cytoplasm. The hnRNP …

**Accessions** — [HGNC:5034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5034) · Entrez [3182](https://www.ncbi.nlm.nih.gov/gene/3182) · UniProt [Q99729](https://www.uniprot.org/uniprotkb/Q99729) · Ensembl [ENSG00000197451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197451)

## Data

Gene col 12400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12400); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12400]; `tensor/DDL_lfc|DDL_z.npy` [12400]; `embed/gene_vectors.npy` [12400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12400 or target_col == 12400). Every well: [[HNRNPAB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPAB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
