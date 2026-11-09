---
symbol: "TTK"
type: "gene"
col: 3401
ensembl_id: "ENSG00000112742"
name: "TTK protein kinase"
location: "6q14.1"
module: 67
arm: "+"
pooled_cpm: 55.46
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# TTK

*TTK protein kinase* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.76× (z +9.6, q 4e-19, up in 34 of 47 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.78× (z +6.4, q 1e-08, up in 33 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (RKO 8.33×, A549 5.87×, PANC-1 3.24×, NCI-H2030 3.44×, …; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (LoVo 6.21×, LS 180 8.58×, KATO III 5.12×, PANC-1 3.58×; ⚠ cell-cycle shift, explains ~69% of this change); [[Digitoxin (drug)]] 5 µM in 4 lines (KATO III 4.90×, LS 180 6.46×, LoVo 4.30×, PANC-1 2.96×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (HEC-1-A 6.16×).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.426× (z -10.3, q 4e-22, down in 35 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.666× (z -7.0, q 4e-10, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUF2]] (+0.93, fdr 7e-06), [[CCNA2]] (+0.89, fdr 7e-06), [[CDCA3]] (+0.88, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3401.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (RKO 8.33×, A549 5.87×, PANC-1 3.24×, NCI-H2030 3.44×, …; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (LoVo 6.21×, LS 180 8.58×, KATO III 5.12×, PANC-1 3.58×; ⚠ cell-cycle shift, explains ~69% of this change); [[Digitoxin (drug)]] 5 µM in 4 lines (KATO III 4.90×, LS 180 6.46×, LoVo 4.30×, PANC-1 2.96×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (HEC-1-A 6.16×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.76×** | +9.6 | 4e-19 | 34/47 (RKO, A549, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **3.55×** | +8.0 | 4e-13 | 40/47 (HT-29, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.84×** | +7.3 | 6e-11 | 37/47 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.81×** | +7.1 | 2e-10 | 31/47 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.78×** | +6.4 | 1e-08 | 33/47 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **1.59×** | +5.4 | 7e-06 | 31/46 (LoVo, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.52×** | +5.1 | 4e-05 | 28/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **2.15×** | +4.8 | 1e-04 | 29/46 (J82, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.45×** | +4.3 | 0.001 | 24/47 (PANC-1, A549, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.42×** | +4.2 | 0.001 | 23/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.41×** | +4.2 | 0.002 | 26/47 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.39×** | +3.9 | 0.004 | 23/47 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.34×** | +3.5 | 0.021 | 21/47 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.30× | +3.0 | 0.10 | 16/47 (RKO, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3401.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.426×** | -10.3 | 4e-22 | 35/45 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.556×** | -10.0 | 3e-21 | 39/47 (A498, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -8.6 | 2e-15 | 30/41 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.528×** | -7.7 | 2e-12 | 38/47 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -7.0 | 4e-10 | 32/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.618×** | -5.5 | 4e-06 | 28/47 (A-172, HT-29, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.659×** | -5.1 | 4e-05 | 24/47 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.663×** | -5.0 | 5e-05 | 26/47 (HEC-1-A, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.694×** | -4.4 | 6e-04 | 23/47 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.674×** | -4.4 | 6e-04 | 27/43 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.686×** | -4.4 | 6e-04 | 25/46 (A498, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.704×** | -4.3 | 1e-03 | 27/47 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.781×** | -4.2 | 0.001 | 24/47 (A498, SW48, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.004 | 29/47 (A498, A-427, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.740×** | -3.6 | 0.010 | 20/47 (NCI-H460, H4, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.741×** | -3.5 | 0.017 | 17/47 (A498, NCI-H2347, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.755×** | -3.4 | 0.022 | 19/47 (HOP62, NCI-H460, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.677×** | -3.4 | 0.024 | 19/47 (RPMI-7951, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.833×** | -3.1 | 0.046 | 16/47 (LoVo, A-427, …) | two highest doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.835× | -3.1 | 0.048 | 22/47 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.782×** | -3.0 | 0.067 | 19/47 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **0.787×** | -2.9 | 0.081 | 12/47 (LOX-IMVI, RKO, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.789×** | -2.9 | 0.088 | 15/46 (C32, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.81 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3401. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 68.9 | 0 | 13 (9 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.123× (z -25.4) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.274× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 68.3 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.250× (z -12.2) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.287× (z -11.0) |
| [[A-172 (line)]] | wt | 35.2 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.169× (z -12.9) ⚠ cell-cycle shift, explains ~76% of this change |
| [[HEC-1-A (line)]] | alt | 99.4 | 2 (1 ⚠) | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 6.16× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -15.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 27.6 | 2 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.58× (z +12.5) ⚠ cell-cycle shift, explains ~69% of this change | [[Selinexor (drug)]] 5 µM 0.219× (z -12.5) ⚠ cell-cycle shift, explains ~65% of this change |
| [[NCI-H460 (line)]] | wt | 33.7 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 0.5 µM 0.237× (z -11.0) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -10.1) |
| [[A-427 (line)]] | wt | 47.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.248× (z -14.9) |
| [[PANC-1 (line)]] | alt | 64.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +15.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 43.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0873× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.206× (z -10.0) |
| [[HOP62 (line)]] | alt | 73.0 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.298× (z -12.6) ⚠ cell-cycle shift, explains ~65% of this change |
| [[LoVo (line)]] | wt | 27.3 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.21× (z +12.9) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[NCI-H2030 (line)]] | alt | 76.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +11.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.143× (z -12.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 124 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -14.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 47.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.87× (z +15.2) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.244× (z -8.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[AN3 CA (line)]] | alt | 172 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -11.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 43.1 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.12× (z +12.0) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 68.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[4EGI-1 (drug)]] 5 µM 0.0407× (z -9.2) |
| [[SW 900 (line)]] | alt | 50.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Belzutifan (drug)]] 5 µM 0.0640× (z -8.7) |
| [[SW48 (line)]] | wt | 71.7 | 0 | 2 (1 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.245× (z -11.2) |
| [[C32 (line)]] | wt | 42.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.334× (z -9.0) ⚠ cell-cycle shift, explains ~65% of this change |
| [[HCT15 (line)]] | alt | 65.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.252× (z -12.0) ⚠ cell-cycle shift, explains ~65% of this change |
| [[Hs 766T (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.190× (z -13.3) ⚠ cell-cycle shift, explains ~65% of this change |
| [[HS-578T (line)]] | alt | 62.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -9.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 40.8 | 1 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.2× (z +9.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[J82 (line)]] | alt | 85.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 50.5 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +8.8) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[Panc 03.27 (line)]] | alt | 42.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 37.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.33× (z +17.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 51.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0923× (z -16.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0895× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 70.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.375× (z -8.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 80.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3401), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUF2]] | +0.93 | +0.93 / +0.94 | both halves | 7e-06 | STRING 989 |
| [[CCNA2]] | +0.89 | +0.88 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 939 |
| [[CDCA3]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | STRING 858 |
| [[RACGAP1]] | +0.88 | +0.88 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 845 |
| [[TOP2A]] | +0.86 | +0.82 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 958 |
| [[NEK2]] | +0.86 | +0.82 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 845 |
| [[CDK1]] | +0.86 | +0.81 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 905 |
| [[CDCA8]] | +0.86 | +0.83 / +0.88 | both halves | 7e-06 | STRING 946 |
| [[CIT]] | +0.86 | +0.82 / +0.87 | both halves | 7e-06 |  |
| [[CKAP2]] | +0.85 | +0.80 / +0.84 | both halves | 7e-06 | STRING 868 |
| [[KIF2C]] | +0.85 | +0.82 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 955 |
| [[PSRC1]] | +0.84 | +0.79 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises TTK's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.32× lower at baseline in the lines without PIMREG | 0.057 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[PBK]] | C | PBK activity raises TTK's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.23× lower at baseline in the lines without PBK | 0.033 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises TTK's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.32× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[NDC80]] | C | NDC80 activity raises TTK's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without NDC80 | 0.072 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises TTK's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.64× lower at baseline in the lines without AURKB | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.879). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.8, -55.2); signed map (-48.4, -40.7). **Vector** length 142, 51.9% of its response variance represented; |z| ≥ 3 in 1,279 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.77 to 12); *Mitotic Prometaphase* (reactome, mean cos +0.73 to 8); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.74 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +4.7 | +3.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +4.5 | +4.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.4 | +1.1 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.5 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +0.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | -7.8 | -5.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -7.2 | -7.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -7.1 | -10.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.9 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -4.4 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.7 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | TTK protein kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:80,003,887-80,042,527 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PYT, MPS1, MPS1L1, CT96, MPH1 |
| Gene groups (HGNC) | TTK protein kinase family |
| Hallmark sets | SPERMATOGENESIS, G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [P33981](https://www.uniprot.org/uniprotkb/P33981) (Dual specificity protein kinase TTK):

> Involved in mitotic spindle assembly checkpoint signaling, a process that delays anaphase until chromosomes are bioriented on the spindle, and in the repair of incorrect mitotic kinetochore-spindle microtubule attachments. Phosphorylates MAD1L1 to promote the mitotic spindle assembly checkpoint. Phosphorylates CDCA8/Borealin leading to enhanced AURKB activity at the kinetochore. Phosphorylates SKA3 at 'Ser-34' leading to dissociation of the SKA complex from microtubules and destabilization of …

**Summary**, from NCBI Gene [7272](https://www.ncbi.nlm.nih.gov/gene/7272):

> This gene encodes a dual specificity protein kinase with the ability to phosphorylate tyrosine, serine and threonine. Associated with cell proliferation, this protein is essential for chromosome alignment at the centromere during mitosis and is required for centrosome duplication. It has been found to be a critical mitotic checkpoint protein for accurate segregation of chromosomes during mitosis. Tumorigenesis may occur when this protein fails to degrade and produces excess centrosomes …

**Accessions** — [HGNC:12401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12401) · Entrez [7272](https://www.ncbi.nlm.nih.gov/gene/7272) · UniProt [P33981](https://www.uniprot.org/uniprotkb/P33981) · Ensembl [ENSG00000112742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112742)

## Data

Gene col 3401: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3401); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3401, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3401]; `tensor/DDL_lfc|DDL_z.npy` [3401]; `embed/gene_vectors.npy` [3401]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3401 or target_col == 3401). Every well: [[TTK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
