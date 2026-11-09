---
symbol: "DBF4"
type: "gene"
col: 121
ensembl_id: "ENSG00000006634"
name: "DBF4-CDC7 kinase regulatory subunit"
location: "7q21.12"
module: 22
arm: "+"
pooled_cpm: 60.9
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# DBF4

*DBF4-CDC7 kinase regulatory subunit* — 7q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.75× (z +19.4, q 0e+00, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~66% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.50× (z +5.5, q 2e-06, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.540× (z -8.0, q 9e-13, down in 30 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.771× (z -4.9, q 1e-04, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A-427 0.226×, A498 0.396×, H4 0.266×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (HCT15 0.114×, HT-29 0.183×, NCI-H1573 0.191×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.319×, SW48 0.242×, AN3 CA 0.183×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.130×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.395×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (CHP-212 0.0934×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNF]] (+0.80, fdr 7e-06), [[G2E3]] (+0.80, fdr 7e-06), [[FAM72D]] (+0.80, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 121.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **2.75×** | +19.4 | 0e+00 | 44/48 (CFPAC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.37×** | +11.7 | 2e-29 | 42/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **2.28×** | +10.7 | 1e-24 | 44/48 (NCI-H460, A-172, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.10×** | +10.1 | 8e-22 | 45/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.87×** | +8.5 | 2e-15 | 43/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.87×** | +8.5 | 2e-15 | 40/48 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.67×** | +6.7 | 2e-09 | 37/47 (NCI-H460, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.60×** | +6.4 | 1e-08 | 35/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.60×** | +6.4 | 1e-08 | 38/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~97% of this change | **1.56×** | +6.1 | 7e-08 | 33/48 (PANC-1, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.28×** | +5.8 | 3e-07 | 36/49 (HEC-1-A, SK-MEL-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +5.5 | 2e-06 | 35/48 (SW480, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.39×** | +4.5 | 3e-04 | 26/48 (NCI-H1792, NCI-H1573, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.24×** | +4.2 | 0.001 | 25/48 (LoVo, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.35×** | +4.1 | 0.002 | 24/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.73×** | +3.9 | 0.003 | 26/48 (A498, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +3.6 | 0.011 | 22/48 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.022 | 21/49 (NCI-H23, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.056 | 16/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.067 | 20/48 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.069 | 20/48 (NCI-H2030, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 121.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A-427 0.226×, A498 0.396×, H4 0.266×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (HCT15 0.114×, HT-29 0.183×, NCI-H1573 0.191×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 0.319×, SW48 0.242×, AN3 CA 0.183×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.130×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.395×); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (CHP-212 0.0934×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.540×** | -8.0 | 9e-13 | 30/42 (HCT15, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.697×** | -6.8 | 2e-09 | 35/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.677×** | -5.2 | 3e-05 | 34/48 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.771×** | -4.9 | 1e-04 | 32/48 (A-427, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.707×** | -4.6 | 4e-04 | 28/48 (HEC-1-A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.724×** | -4.3 | 0.001 | 25/48 (A498, C32, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.724×** | -4.3 | 0.001 | 35/48 (NCI-H460, A549, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.744×** | -4.0 | 0.005 | 29/49 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.771×** | -3.5 | 0.032 | 22/48 (A-172, H4, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.772×** | -3.3 | 0.047 | 25/48 (HEC-1-A, A498, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.773×** | -3.3 | 0.047 | 20/48 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.787×** | -3.1 | 0.099 | 23/49 (AN3 CA, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | 0.787× | -3.0 | 0.11 | 22/48 (SW480, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.96 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 48.2 | 11 (10 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +17.9) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Gefitinib (drug)]] 5 µM 2.66× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -9.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 67.3 | 4 (4 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.1) ⚠ cell-cycle shift, explains ~66% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -13.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 70.5 | 2 (2 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +16.0) ⚠ cell-cycle shift, explains ~66% of this change | [[Selinexor (drug)]] 5 µM 0.396× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 48.5 | 3 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +16.6) ⚠ cell-cycle shift, explains ~66% of this change | [[Selinexor (drug)]] 5 µM 0.384× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 66.5 | 2 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.74× (z +10.8) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.266× (z -11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.373× (z -8.6) |
| [[A-427 (line)]] | wt | 89.4 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.226× (z -18.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.395× (z -11.2) |
| [[C32 (line)]] | wt | 101 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +15.5) ⚠ cell-cycle shift, explains ~66% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.282× (z -9.4) ⚠ cell-cycle shift, explains ~72% of this change |
| [[HOP62 (line)]] | alt | 47.3 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.30× (z +11.8) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 36.3 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.89× (z +14.7) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[PANC-1 (line)]] | alt | 74.7 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.5) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[SW48 (line)]] | wt | 131 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.6) ⚠ cell-cycle shift, explains ~66% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -11.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 34.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +18.5) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[Hs 766T (line)]] | wt | 45.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +10.4) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[KATO III (line)]] | alt | 70.2 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +14.1) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[LS 180 (line)]] | wt | 51.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +8.9) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 0.5 µM 0.308× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 37.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +11.8) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[NCI-H2030 (line)]] | alt | 49.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +17.0) ⚠ cell-cycle shift, explains ~66% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -10.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 143 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -11.9) |
| [[J82 (line)]] | alt | 56.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +12.9) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[LOX-IMVI (line)]] | wt | 40.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.1) ⚠ cell-cycle shift, explains ~66% of this change | [[Selinexor (drug)]] 5 µM 0.388× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 33.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.2) ⚠ cell-cycle shift, explains ~66% of this change | [[Dinaciclib (drug)]] 5 µM 0.191× (z -10.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 46.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +16.5) ⚠ cell-cycle shift, explains ~66% of this change | [[Selinexor (drug)]] 5 µM 0.425× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 67.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +10.7) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 65.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +13.4) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[A549 (line)]] | wt | 48.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +14.1) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[AsPC-1 (line)]] | alt | 35.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.2) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[CHP-212 (line)]] | wt | 38.7 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0934× (z -8.8) |
| [[COLO 205 (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +10.0) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[HCT15 (line)]] | alt | 62.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -13.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 44.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +11.4) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[HT-29 (line)]] | alt | 74.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -11.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 61.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.3) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[NCI-H2347 (line)]] | alt | 57.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +13.6) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[RKO (line)]] | wt | 79.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.7) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[SHP-77 (line)]] | alt | 79.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -9.4) ⚠ cell-cycle shift, explains ~65% of this change |
| [[SNU-423 (line)]] | alt | 50.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +12.3) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[SW 900 (line)]] | alt | 53.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.4) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[SW1417 (line)]] | alt | 90.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +14.2) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[BT-474 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 90.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNF]] | +0.80 | +0.74 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[G2E3]] | +0.80 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[FAM72D]] | +0.80 | +0.80 / +0.78 | both halves | 7e-06 |  |
| [[CENPE]] | +0.80 | +0.81 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[CKAP2]] | +0.79 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[KIF20B]] | +0.79 | +0.73 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 475 |
| [[NDC80]] | +0.79 | +0.78 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[CDCA8]] | +0.78 | +0.71 / +0.81 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[CENPF]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[SGO2]] | +0.78 | +0.76 / +0.79 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 431 |
| [[CDKN3]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[GAS2L3]] | +0.76 | +0.80 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises DBF4's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.92× lower at baseline in the lines without PIMREG | 0.005 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises DBF4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises DBF4's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[CDC20]] | C | CDC20 activity raises DBF4's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.11× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[FAM72D]] | C | FAM72D activity raises DBF4's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 1.87× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[NDC80]] | C | NDC80 activity raises DBF4's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 1.93× lower at baseline in the lines without NDC80 | 0.072 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises DBF4's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without AURKB | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises DBF4's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.736). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.3, -57.3); signed map (-50.9, -42.0). **Vector** length 132, 48.4% of its response variance represented; |z| ≥ 3 in 1,259 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.68 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.55 to 48); *E2F targets* (hallmark, mean cos +0.54 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +7.9 | +19.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.2 | +5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.3 | +3.6 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | +4.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~97% of this change | +4.3 | +6.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | -0.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.5 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.1 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.4 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.0 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | -1.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -6.1 | -3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.8 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -0.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | DBF4-CDC7 kinase regulatory subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.12 — chr7:87,876,216-87,909,553 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ASK, chif, ZDBF1, DBF4A |
| Gene groups (HGNC) | Zinc fingers DBF-type |
| Hallmark sets | SPERMATOGENESIS, G2M_CHECKPOINT |
| Reactome | 10 pathways, smallest: Activation of the pre-replicative complex; Activation of ATR in response to replication stress; DNA Replication Pre-Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBU7](https://www.uniprot.org/uniprotkb/Q9UBU7) (Protein DBF4 homolog A):

> Regulatory subunit for CDC7 which activates its kinase activity thereby playing a central role in DNA replication and cell proliferation. Required for progression of S phase. The complex CDC7-DBF4A selectively phosphorylates MCM2 subunit at 'Ser-40' and 'Ser-53' and then is involved in regulating the initiation of DNA replication during cell cycle.

**Summary**, from NCBI Gene [10926](https://www.ncbi.nlm.nih.gov/gene/10926):

> Predicted to enable protein serine/threonine kinase activator activity. Predicted to be involved in positive regulation of nuclear cell cycle DNA replication and regulation of cell cycle phase transition. Located in nuclear body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17364](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17364) · Entrez [10926](https://www.ncbi.nlm.nih.gov/gene/10926) · UniProt [Q9UBU7](https://www.uniprot.org/uniprotkb/Q9UBU7) · Ensembl [ENSG00000006634](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006634)

## Data

Gene col 121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 121); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 121]; `tensor/DDL_lfc|DDL_z.npy` [121]; `embed/gene_vectors.npy` [121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 121 or target_col == 121). Every well: [[DBF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DBF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
