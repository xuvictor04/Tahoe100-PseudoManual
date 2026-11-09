---
symbol: "TSNAX-DISC1"
type: "gene"
col: 15654
ensembl_id: "ENSG00000270106"
name: "TSNAX-DISC1 readthrough (NMD candidate)"
location: "1q42.2"
module: 37
arm: "+"
pooled_cpm: 21.49
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# TSNAX-DISC1

*TSNAX-DISC1 readthrough (NMD candidate)* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.10× (z +17.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (13 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.400× (z -10.3, q 4e-22, down in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.401× (z -5.6, q 2e-06, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 0.146×, HEC-1-A 0.112×, SW 900 0.101×, RPMI-7951 0.0984×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Digitoxin (drug)]] 5 µM in 3 lines (HepG2/C3A 0.0721×, PANC-1 0.194×, BT-474 0.0625×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C32 0.136×, HCT15 0.0878×, H4 0.0849×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.202×); [[TAK-901 (drug)]] 5 µM in 1 line (SNU-1 0.0581×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02680]] (+0.78, fdr 7e-06), [[C9orf153]] (+0.74, fdr 7e-06), [[WDR49]] (+0.73, fdr 7e-06); moves opposite to [[CEP41]] (-0.56, fdr 2e-05), [[RASAL2]] (-0.55, fdr 3e-05), [[ROCK2]] (-0.54, fdr 3e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15654.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +17.1 | 0e+00 | 48/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +10.3 | 2e-22 | 38/46 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.89×** | +9.7 | 4e-20 | 39/48 (A498, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +8.9 | 7e-17 | 37/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +8.6 | 6e-16 | 36/48 (A-172, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +6.8 | 1e-09 | 38/48 (SHP-77, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +5.6 | 2e-06 | 29/48 (SHP-77, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +4.9 | 8e-05 | 26/48 (SW480, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.52×** | +3.8 | 0.009 | 22/48 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.46×** | +3.6 | 0.018 | 17/48 (LOX-IMVI, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.69×** | +3.2 | 0.065 | 11/47 (Panc 03.27, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15654.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 0.146×, HEC-1-A 0.112×, SW 900 0.101×, RPMI-7951 0.0984×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Digitoxin (drug)]] 5 µM in 3 lines (HepG2/C3A 0.0721×, PANC-1 0.194×, BT-474 0.0625×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C32 0.136×, HCT15 0.0878×, H4 0.0849×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.202×); [[TAK-901 (drug)]] 5 µM in 1 line (SNU-1 0.0581×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.400×** | -10.3 | 4e-22 | 37/47 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.449×** | -9.4 | 2e-18 | 31/43 (C32, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.450×** | -9.0 | 5e-17 | 23/33 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.522×** | -7.6 | 4e-12 | 31/46 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.524×** | -7.3 | 4e-11 | 35/47 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.536×** | -6.8 | 1e-09 | 25/40 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.609×** | -5.8 | 5e-07 | 32/48 (PANC-1, AsPC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.401×** | -5.6 | 2e-06 | 32/48 (SNU-1, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.646×** | -5.1 | 2e-05 | 24/48 (PANC-1, H4, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.690×** | -3.8 | 0.007 | 23/48 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.785×** | -3.5 | 0.022 | 23/47 (A498, COLO 205, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.742×** | -3.5 | 0.022 | 18/48 (PANC-1, HepG2/C3A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.744×** | -3.5 | 0.022 | 20/48 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.751×** | -3.4 | 0.031 | 19/48 (A-427, NCI-H460, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.741×** | -3.1 | 0.073 | 18/48 (NCI-H1573, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.9 | 4 (1 ⚠) | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -10.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 27.1 | 1 | 8 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 20.8 | 2 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -17.5) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 66.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.202× (z -11.3) |
| [[SW 900 (line)]] | alt | 36.3 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 20.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 12.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.84× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -10.4) ⚠ cell-cycle shift, explains ~59% of this change |
| [[H4 (line)]] | wt | 40.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0849× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 13.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.74× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.177× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +12.0) | [[Harringtonine (drug)]] 5 µM 0.191× (z -9.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RPMI-7951 (line)]] | alt | 32.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0984× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SNU-1 (line)]] | wt | 43.1 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.144× (z -10.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0581× (z -8.7) |
| [[SNU-423 (line)]] | alt | 26.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 12.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +10.2) | — |
| [[A-427 (line)]] | wt | 28.5 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.175× (z -10.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[COLO 205 (line)]] | alt | 24.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 48.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0878× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 27.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 38.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0721× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[hTERT-HPNE (line)]] | wt | 33.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 10.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.106× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 13.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +11.1) | [[Digitoxin (drug)]] 5 µM 0.217× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.111× (z -13.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RKO (line)]] | wt | 9.11 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.97× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.58× (z +10.0) ⚠ cell-cycle shift, explains ~39% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 13.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.134× (z -9.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0625× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[CFPAC-1 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.82× (z +13.0) | — |
| [[Hs 766T (line)]] | wt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 23.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +10.4) | — |
| [[KATO III (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.209× (z -8.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H1792 (line)]] | alt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.10× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 25.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 17.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02680]] | +0.78 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[C9orf153]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[WDR49]] | +0.73 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[PMS2P4-1]] | +0.71 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[ADAM20]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CD200R1]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[VDAC1P8]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[GLE1]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[GET1-SH3BGR]] | +0.66 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[TEX29]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[NOXRED1]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP41]] | -0.56 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[RASAL2]] | -0.55 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[ROCK2]] | -0.54 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[CENPB]] | -0.52 | -0.47 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TSNAX-DISC1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.3, -18.9); signed map (9.7, 5.4). **Vector** length 110, 30.7% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +17.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +10.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +8.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.1 | +9.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +4.3 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +0.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.8 | +0.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -6.3 | -10.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.2 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -4.4 | -9.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | -4.1 | -7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.0 | -3.8 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.6 | -2.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.5 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | TSNAX-DISC1 readthrough (NMD candidate) |
| Locus type | readthrough (other) |
| Location | 1q42.2 — chr1:231,528,653-231,819,244 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100303453](https://www.ncbi.nlm.nih.gov/gene/100303453):

> This gene represents naturally occurring read-through transcription between the neighboring TSNAX (translin-associated factor X) and DISC1 (disrupted in schizophrenia 1) genes on chromosome 1. Alternative splicing results in multiple transcript variants, all of which are candidates for nonsense-mediated mRNA decay (NMD) and are unlikely to be protein-coding. These alterations in gene processing may be associated with risk for psychiatric illness, most notably, schizophrenia. [provided by …

**Accessions** — [HGNC:49177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49177) · Entrez [100303453](https://www.ncbi.nlm.nih.gov/gene/100303453) · Ensembl [ENSG00000270106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270106)

## Data

Gene col 15654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15654); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15654]; `tensor/DDL_lfc|DDL_z.npy` [15654]; `embed/gene_vectors.npy` [15654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15654 or target_col == 15654). Every well: [[TSNAX-DISC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSNAX-DISC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
