---
symbol: "PCYT1A"
type: "gene"
col: 8422
ensembl_id: "ENSG00000161217"
name: "phosphate cytidylyltransferase 1A, choline"
location: "3q29"
module: 72
arm: "+"
pooled_cpm: 78.64
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PCYT1A

*phosphate cytidylyltransferase 1A, choline* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.49× (z +29.3, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.05 µM: 0.796× (z -6.8, q 6e-09, down in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.187×, Panc 03.27 0.402×, H4 0.338×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HS-578T 0.511×, A498 0.612×, A-172 0.612×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-1 0.151×, NCI-H1573 0.360×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (CHP-212 0.109×); [[Sonidegib (drug)]] 0.5 µM in 1 line (NCI-H661 0.0568×); [[Tucidinostat (drug)]] 5 µM in 1 line (HS-578T 0.631×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFAND2A]] (+0.74, fdr 7e-06), [[TANGO2]] (+0.70, fdr 7e-06), [[YKT6]] (+0.69, fdr 7e-06); moves opposite to [[SINHCAF]] (-0.59, fdr 1e-05), [[TBL1XR1]] (-0.58, fdr 3e-05), [[FOXP1]] (-0.58, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RPSAP58]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8422.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.49×** | +29.3 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.20×** | +25.3 | 0e+00 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.44×** | +24.2 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +13.5 | 4e-39 | 40/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.60×** | +10.8 | 3e-25 | 38/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +10.1 | 5e-22 | 33/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +8.3 | 1e-14 | 30/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +7.2 | 6e-11 | 26/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +6.7 | 2e-09 | 26/45 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.20× | +5.8 | 4e-07 | 23/48 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.2 | 8e-06 | 23/48 (COLO 205, RKO, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +4.4 | 6e-04 | 14/48 (CFPAC-1, NCI-H1573, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | 1.14× | +4.1 | 0.002 | 16/47 (HCT15, A-427, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +4.0 | 0.003 | 5/48 (LoVo, A549, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.003 | 12/48 (HEC-1-A, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.007 | 7/48 (HEC-1-A, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.008 | 10/48 (LoVo, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.029 | 12/48 (CFPAC-1, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.10× | +3.1 | 0.042 | 3/48 (CFPAC-1, SW 1088, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8422.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.187×, Panc 03.27 0.402×, H4 0.338×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HS-578T 0.511×, A498 0.612×, A-172 0.612×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-1 0.151×, NCI-H1573 0.360×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (CHP-212 0.109×); [[Sonidegib (drug)]] 0.5 µM in 1 line (NCI-H661 0.0568×); [[Tucidinostat (drug)]] 5 µM in 1 line (HS-578T 0.631×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.05 µM |  | **0.796×** | -6.8 | 6e-09 | 25/47 (A549, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | **0.818×** | -6.5 | 3e-08 | 23/49 (RKO, Panc 03.27, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | **0.825×** | -5.7 | 2e-06 | 22/44 (SNU-1, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.898× | -4.9 | 1e-04 | 14/48 (HS-578T, RPMI-7951, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.957× | -4.7 | 3e-04 | 1/50 (NCI-H661) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | 0.878× | -4.2 | 0.002 | 19/48 (H4, KATO III, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.919× | -3.9 | 0.009 | 2/48 (CHP-212, SNU-1) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.892× | -3.7 | 0.015 | 16/48 (H4, HOP62, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.923× | -3.6 | 0.017 | 6/48 (RPMI-7951, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.904× | -3.1 | 0.088 | 13/48 (A-172, RPMI-7951, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.907× | -3.1 | 0.088 | 5/48 (COLO 205, A-427, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | 0.906× | -3.1 | 0.11 | 17/48 (A-172, HS-578T, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8422. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 147 | 2 | 6 (6 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.96× (z +9.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.312× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 93.3 | 3 | 5 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.48× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.419× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 147 | 2 | 5 (5 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.11× (z +10.1) | [[Harringtonine (drug)]] 0.5 µM 0.430× (z -13.6) ⚠ cell-cycle shift, explains ~81% of this change |
| [[SW480 (line)]] | alt | 89.0 | 6 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.82× (z +17.1) | — |
| [[hTERT-HPNE (line)]] | wt | 82.3 | 2 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.80× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.389× (z -8.5) |
| [[C32 (line)]] | wt | 53.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.46× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 86.9 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.92× (z +16.1) | — |
| [[HEC-1-A (line)]] | alt | 88.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.79× (z +15.1) | — |
| [[HS-578T (line)]] | alt | 123 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.631× (z -8.7) |
| [[HT-29 (line)]] | alt | 58.1 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.18× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 69.4 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.32× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[NCI-H460 (line)]] | wt | 54.8 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.58× (z +14.1) | — |
| [[Panc 03.27 (line)]] | alt | 106 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.72× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[PANC-1 (line)]] | alt | 89.3 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.24× (z +23.1) | — |
| [[BT-474 (line)]] | alt | 69.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.64× (z +13.6) | — |
| [[KATO III (line)]] | alt | 82.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.65× (z +11.7) | — |
| [[LOX-IMVI (line)]] | wt | 62.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.78× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 66.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.52× (z +14.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 127 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.01× (z +15.3) | — |
| [[NCI-H1792 (line)]] | alt | 65.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.18× (z +13.3) | — |
| [[NCI-H23 (line)]] | alt | 50.6 | 3 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 3.90× (z +12.2) | — |
| [[SW1417 (line)]] | alt | 81.5 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.86× (z +11.3) | — |
| [[A-427 (line)]] | wt | 57.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.42× (z +10.2) | — |
| [[A498 (line)]] | wt | 90.7 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.02× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.612× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 54.1 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.42× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HepG2_C3A (line)]] | wt | 68.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.52× (z +10.8) | — |
| [[LoVo (line)]] | wt | 59.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.94× (z +13.4) | — |
| [[NCI-H2030 (line)]] | alt | 63.5 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.96× (z +12.5) | — |
| [[RKO (line)]] | wt | 61.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[SNU-423 (line)]] | alt | 66.0 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.588× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 43.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.19× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 63.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.16× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 63.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.109× (z -11.3) |
| [[Hs 766T (line)]] | wt | 62.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.58× (z +9.2) | — |
| [[NCI-H661 (line)]] | alt | 60.2 | 0 | 1 | — | [[Sonidegib (drug)]] 0.5 µM 0.0568× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 87.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.419× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SNU-1 (line)]] | wt | 65.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[SW 900 (line)]] | alt | 76.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.31× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8422), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFAND2A]] | +0.74 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[TANGO2]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[YKT6]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[RPS6KC1]] | +0.67 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[SNX29]] | +0.66 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[FAM219A]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[BRF2]] | +0.64 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[AAK1]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[KCTD21]] | +0.63 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[PSMD13]] | +0.63 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[SLC30A6]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SINHCAF]] | -0.59 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[TBL1XR1]] | -0.58 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[FOXP1]] | -0.58 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[YAP1]] | -0.57 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[SKA2]] | -0.56 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[ECT2]] | -0.55 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[ZDHHC23]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[NFKB1]] | -0.54 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[ZNF608]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[PAXIP1-DT]] | -0.53 | -0.57 / -0.36 | both halves | 9e-05 |  |
| [[NUDT6]] | -0.53 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[TNFAIP2]] | -0.52 | -0.42 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPSAP58]] | B | RPSAP58 activity raises PCYT1A's level | lines that do not express RPSAP58 (22) vs lines expressing it (28) | 1.08× lower at baseline in the lines without RPSAP58 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF681, ENSG00000268119, ANOS1 |
| [[TNFAIP6]] | B | TNFAIP6 activity weakens PCYT1A's drug response | lines that do not express TNFAIP6 (31) vs lines expressing it (18) | the lines without TNFAIP6 respond 1.53× as strongly (z diff -1.47); strongest at Panobinostat 5 µM: 1.52x vs 1.06x (z diff -3.9) | 0.071 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF; target measured in part of the lines; artifact flags |
| [[PTX3]] | B | PTX3 activity raises PCYT1A's level | lines that do not express PTX3 (24) vs lines expressing it (26) | 1.35× lower at baseline in the lines without PTX3 | 0.083 | ⚠ within organs, on part of the lines; also absent: IL7R, RNF182, COL5A1 |
| [[NCEH1]] | B | NCEH1 activity raises PCYT1A's level | lines that do not express NCEH1 (6) vs lines expressing it (44) | 1.37× lower at baseline in the lines without NCEH1 | 0.092 | ⚠ within organs, on part of the lines; also absent: KCNK6, SMCO2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.0, -8.0); signed map (-28.1, -25.7). **Vector** length 122, 33.3% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +13.0 | +24.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +12.7 | +29.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +11.3 | +25.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.9 | +13.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.2 | +6.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.3 | +10.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +2.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -5.0 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.8 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -4.8 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | phosphate cytidylyltransferase 1A, choline |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,214,222-196,287,957 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CT, CTPCT, CCTalpha; previously PCYT1 |
| Reactome | 4 pathways, smallest: Synthesis of PC; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P49585](https://www.uniprot.org/uniprotkb/P49585) (Choline-phosphate cytidylyltransferase A):

> Catalyzes the key rate-limiting step in the CDP-choline pathway for phosphatidylcholine biosynthesis.

**Summary**, from NCBI Gene [5130](https://www.ncbi.nlm.nih.gov/gene/5130):

> This gene belongs to the cytidylyltransferase family and is involved in the regulation of phosphatidylcholine biosynthesis. Mutations in this gene are associated with spondylometaphyseal dysplasia with cone-rod dystrophy. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:8754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8754) · Entrez [5130](https://www.ncbi.nlm.nih.gov/gene/5130) · UniProt [P49585](https://www.uniprot.org/uniprotkb/P49585) · Ensembl [ENSG00000161217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161217)

## Data

Gene col 8422: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8422); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8422, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8422]; `tensor/DDL_lfc|DDL_z.npy` [8422]; `embed/gene_vectors.npy` [8422]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8422 or target_col == 8422). Every well: [[PCYT1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCYT1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
