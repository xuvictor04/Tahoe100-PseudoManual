---
symbol: "PRKN"
type: "gene"
col: 11665
ensembl_id: "ENSG00000185345"
name: "parkin RBR E3 ubiquitin protein ligase"
location: "6q26"
module: 10
arm: "+"
pooled_cpm: 123.93
n_lines_expressing: 42
n_dd_up: 0
n_dd_down: 46
n_dd_up_clean: 0
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 1
direction_downstream: 16
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# PRKN

*parkin RBR E3 ubiquitin protein ligase* — 6q26

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 5.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LoVo 3.45×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.289× (z -18.9, q 0e+00, down in 39 of 40 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.182× (z -18.4, q 0e+00, down in 39 of 40 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGGY]] (+0.56, fdr 3e-05), [[GMDS-DT]] (+0.54, fdr 1e-05), [[C1QTNF3-AMACR]] (+0.54, fdr 4e-05); moves opposite to [[ELF4]] (-0.43, fdr 1e-04), [[DGKA]] (-0.42, fdr 3e-04), [[DEF6]] (-0.41, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WWOX]] → it (grade B ⚠); 16 go from it, the strongest it → [[WDPCP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11665.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 5.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LoVo 3.45×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 1.39× | +3.5 | 0.14 | 21/39 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Omeprazole (drug)]] 5 µM |  | 1.37× | +3.5 | 0.14 | 24/40 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.36× | +3.4 | 0.15 | 23/40 (A549, SNU-423, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.33× | +3.2 | 0.21 | 18/40 (KATO III, LoVo, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.49× | +3.1 | 0.21 | 17/40 (SNU-423, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.32× | +3.1 | 0.21 | 18/40 (PANC-1, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11665.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.289×** | -18.9 | 0e+00 | 39/40 (NCI-H460, A-172, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.174×** | -18.8 | 0e+00 | 39/40 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.182×** | -18.4 | 0e+00 | 39/40 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.228×** | -15.9 | 0e+00 | 40/40 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.248×** | -14.4 | 3e-45 | 38/40 (NCI-H460, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.263×** | -13.8 | 2e-41 | 39/39 (SW 900, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.277×** | -13.8 | 2e-41 | 37/40 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.290×** | -13.3 | 1e-38 | 38/40 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.297×** | -13.1 | 3e-37 | 37/40 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.197×** | -9.1 | 4e-18 | 38/40 (A-427, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.425×** | -8.8 | 5e-17 | 37/39 (A549, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.212×** | -8.7 | 1e-16 | 38/41 (HT-29, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.454×** | -8.5 | 1e-15 | 36/40 (RKO, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.409×** | -7.9 | 1e-13 | 37/40 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.510×** | -7.2 | 2e-11 | 34/40 (PANC-1, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.514×** | -7.1 | 3e-11 | 34/40 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.456×** | -6.9 | 1e-10 | 30/40 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.531×** | -6.4 | 4e-09 | 30/40 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.695×** | -5.5 | 1e-06 | 31/40 (HEC-1-A, AN3 CA, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.649×** | -4.4 | 2e-04 | 29/40 (KATO III, HS-578T, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 671 | 0 | 27 (16 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0667× (z -28.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0903× (z -18.0) |
| [[PANC-1 (line)]] | alt | 119 | 0 | 15 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0924× (z -20.0) |
| [[A549 (line)]] | wt | 108 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0921× (z -23.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0972× (z -15.5) |
| [[A-172 (line)]] | wt | 139 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -24.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -17.5) |
| [[HS-578T (line)]] | alt | 171 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0932× (z -23.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0705× (z -18.5) |
| [[KATO III (line)]] | alt | 153 | 0 | 13 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0945× (z -18.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -18.4) |
| [[A-427 (line)]] | wt | 117 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0963× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.178× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 60.4 | 0 | 12 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 101 | 0 | 12 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.130× (z -14.1) |
| [[HT-29 (line)]] | alt | 607 | 0 | 11 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.116× (z -21.0) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.0583× (z -15.0) |
| [[SNU-423 (line)]] | alt | 169 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -15.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0990× (z -15.4) |
| [[SW480 (line)]] | alt | 63.1 | 0 | 11 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -15.4) |
| [[C32 (line)]] | wt | 129 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -16.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -14.0) |
| [[LoVo (line)]] | wt | 53.5 | 2 (2 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.10× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | [[Digitoxin (drug)]] 0.5 µM 0.212× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 146 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -17.4) |
| [[SW 900 (line)]] | alt | 112 | 0 | 10 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0141× (z -31.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 99.0 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -14.5) |
| [[HOP62 (line)]] | alt | 134 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -22.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -16.4) |
| [[C-33 A (line)]] | alt | 117 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0924× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 65.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -15.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 62.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -18.8) |
| [[SHP-77 (line)]] | alt | 91.6 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -14.8) |
| [[AN3 CA (line)]] | alt | 170 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0415× (z -17.1) |
| [[COLO 205 (line)]] | alt | 61.5 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0918× (z -16.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -12.8) |
| [[SNU-1 (line)]] | wt | 68.1 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0752× (z -13.7) |
| [[SW 1088 (line)]] | alt | 180 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0239× (z -13.8) |
| [[A498 (line)]] | wt | 80.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -18.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.173× (z -12.0) |
| [[H4 (line)]] | wt | 78.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -13.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.156× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 52.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -11.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -10.0) |
| [[SW1417 (line)]] | alt | 47.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -10.9) |
| [[SW48 (line)]] | wt | 134 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.120× (z -12.5) |
| [[CHP-212 (line)]] | wt | 90.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -9.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 53.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -12.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 39.9 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.207× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 172 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.119× (z -11.7) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.147× (z -10.9) |
| [[RKO (line)]] | wt | 55.1 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.141× (z -13.3) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -8.9) |
| [[SW 1271 (line)]] | alt | 128 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0618× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0623× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 63.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.236× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.3 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 23.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGGY]] | +0.56 | +0.58 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[GMDS-DT]] | +0.54 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[C1QTNF3-AMACR]] | +0.54 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[BABAM2]] | +0.50 | +0.52 / +0.48 | both halves | 2e-05 | pathway: Deubiquitination |
| [[NBEA]] | +0.50 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[WDPCP]] | +0.49 | +0.29 / +0.50 | both halves | 2e-04 |  |
| [[FAM172A]] | +0.49 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[CCDC102B]] | +0.47 | +0.55 / +0.36 | both halves | 9e-05 |  |
| [[CCDC7]] | +0.47 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[SPATA17]] | +0.47 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[ZBTB20]] | +0.46 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[LINC01013]] | +0.46 | +0.42 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELF4]] | -0.43 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[DGKA]] | -0.42 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[DEF6]] | -0.41 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[MYORG]] | -0.40 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ZDHHC13]] | -0.40 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[LPAR5]] | -0.40 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[ST6GALNAC2]] | -0.39 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[INPP5E]] | -0.39 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[NIPAL1]] | -0.39 | -0.26 / -0.33 | both halves | 4e-04 |  |
| [[SULF2]] | -0.39 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[KHDC1]] | -0.38 | -0.27 / -0.25 | both halves | 4e-04 |  |
| [[RABGEF1P3]] | -0.38 | -0.30 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WWOX]] | B | WWOX activity raises PRKN's level | lines that do not express WWOX (5) vs lines expressing it (45) | 2.96× lower at baseline in the lines without WWOX | 0.072 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDPCP]] | B | PRKN activity raises WDPCP's level | lines that do not express PRKN (8) vs lines expressing it (42) | 2.35× lower at baseline in the lines without PRKN | 0.011 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[BABAM2]] | B | PRKN activity raises BABAM2's level | lines that do not express PRKN (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without PRKN | 0.013 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[WWOX]] | B | PRKN activity raises WWOX's level | lines that do not express PRKN (8) vs lines expressing it (42) | 2.75× lower at baseline in the lines without PRKN | 0.018 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[ANKRD24]] | B | PRKN activity raises ANKRD24's level | lines that do not express PRKN (8) vs lines expressing it (42) | 2.06× lower at baseline in the lines without PRKN | 0.020 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[LINC01572]] | B | PRKN activity raises LINC01572's level | lines that do not express PRKN (8) vs lines expressing it (42) | 2.19× lower at baseline in the lines without PRKN | 0.030 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[IMMP2L]] | B | PRKN activity raises IMMP2L's level | lines that do not express PRKN (8) vs lines expressing it (42) | 1.94× lower at baseline in the lines without PRKN | 0.032 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[FBXO15]] | B | PRKN activity raises FBXO15's level | lines that do not express PRKN (8) vs lines expressing it (42) | 1.82× lower at baseline in the lines without PRKN | 0.041 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[SPATA17]] | B | PRKN activity raises SPATA17's level | lines that do not express PRKN (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without PRKN | 0.043 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[CASC2]] | B | PRKN activity raises CASC2's level | lines that do not express PRKN (8) vs lines expressing it (42) | 2.12× lower at baseline in the lines without PRKN | 0.044 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[C11orf65]] | B | PRKN activity raises C11orf65's level | lines that do not express PRKN (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without PRKN | 0.045 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[CCDC171]] | B | PRKN activity raises CCDC171's level | lines that do not express PRKN (8) vs lines expressing it (42) | 2.41× lower at baseline in the lines without PRKN | 0.062 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[CALN1]] | B | PRKN activity raises CALN1's level | lines that do not express PRKN (8) vs lines expressing it (42) | 2.10× lower at baseline in the lines without PRKN | 0.067 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.179). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-24.3, 32.3); signed map (2.2, 6.0). **Vector** length 76.1, 24.5% of its response variance represented; |z| ≥ 3 in 1,540 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | -18.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.6 | -18.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | +3.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.6 | +1.7 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 5 µM |  | +1.3 | +1.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +1.3 | +1.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.0 | -13.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.9 | -7.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.4 | -5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | -3.6 | -6.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.2 | -3.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -2.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.3 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | parkin RBR E3 ubiquitin protein ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q26 — chr6:161,347,417-162,727,775 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PDJ, AR-JP, parkin; previously PARK2 |
| Gene groups (HGNC) | Ring finger proteins; RBR E3 ubiquitin ligases |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 16 pathways, smallest: Josephin domain DUBs; RIPK1-mediated regulated necrosis; Regulation of necroptotic cell death |
| Matched by | ensembl_id |

**Function**, from UniProt [O60260](https://www.uniprot.org/uniprotkb/O60260) (E3 ubiquitin-protein ligase parkin):

> Functions within a multiprotein E3 ubiquitin ligase complex, catalyzing the covalent attachment of ubiquitin moieties onto substrate proteins. Substrates include SYT11 and VDAC1. Other substrates are BCL2, CCNE1, GPR37, RHOT1/MIRO1, MFN1, MFN2, STUB1, SNCAIP, SEPTIN5, TOMM20, USP30, ZNF746, MIRO1 and AIMP2. Mediates monoubiquitination as well as 'Lys-6', 'Lys-11', 'Lys-48'-linked and 'Lys-63'-linked polyubiquitination of substrates depending on the context. Participates in the removal and/or …

**Summary**, from NCBI Gene [5071](https://www.ncbi.nlm.nih.gov/gene/5071):

> The precise function of this gene is unknown; however, the encoded protein is a component of a multiprotein E3 ubiquitin ligase complex that mediates the targeting of substrate proteins for proteasomal degradation. Mutations in this gene are known to cause Parkinson disease and autosomal recessive juvenile Parkinson disease. Alternative splicing of this gene produces multiple transcript variants encoding distinct isoforms. Additional splice variants of this gene have been described but …

**Accessions** — [HGNC:8607](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8607) · Entrez [5071](https://www.ncbi.nlm.nih.gov/gene/5071) · UniProt [O60260](https://www.uniprot.org/uniprotkb/O60260) · Ensembl [ENSG00000185345](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185345)

## Data

Gene col 11665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11665); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11665]; `tensor/DDL_lfc|DDL_z.npy` [11665]; `embed/gene_vectors.npy` [11665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11665 or target_col == 11665). Every well: [[PRKN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
