---
symbol: "FAM219A"
type: "gene"
col: 9045
ensembl_id: "ENSG00000164970"
name: "family with sequence similarity 219 member A"
location: "9p13.3"
module: 72
arm: "+"
pooled_cpm: 98.83
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# FAM219A

*family with sequence similarity 219 member A* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 3.52× (z +17.4, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.347× (z -14.9, q 0e+00, down in 30 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.817× (z -4.2, q 0.001, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C9orf24]] (+0.74, fdr 7e-06, ⚠ same locus), [[P4HA2]] (+0.71, fdr 7e-06), [[ABCB6]] (+0.66, fdr 7e-06), [[PCYT1A]] (+0.66, fdr 7e-06); moves opposite to [[NAPEPLD]] (-0.61, fdr 1e-05), [[PUM2]] (-0.59, fdr 1e-04), [[TGFBR2]] (-0.58, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LOXL2]] → it (grade B ⚠); 2 go from it, the strongest it → [[ANKRD39]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9045.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **3.52×** | +17.4 | 0e+00 | 45/45 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.19×** | +17.0 | 0e+00 | 45/45 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.72×** | +14.7 | 0e+00 | 44/45 (SW480, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.88×** | +6.0 | 3e-07 | 32/46 (SW480, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **2.16×** | +5.9 | 4e-07 | 29/42 (LS 180, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.3 | 9e-06 | 23/46 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 9e-05 | 28/44 (SW 900, SK-MEL-2, …) | two highest doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.36×** | +4.3 | 1e-03 | 27/44 (RPMI-7951, SW480, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.007 | 23/45 (HT-29, COLO 205, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.30×** | +3.8 | 0.008 | 24/45 (COLO 205, HepG2/C3A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.28×** | +3.6 | 0.018 | 21/45 (SW48, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9045.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.347×** | -14.9 | 0e+00 | 30/39 (hTERT-HPNE, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.404×** | -13.3 | 5e-38 | 36/44 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.444×** | -11.1 | 4e-26 | 32/40 (J82, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.460×** | -11.0 | 6e-26 | 34/44 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.606×** | -7.1 | 1e-10 | 28/44 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.618×** | -7.1 | 1e-10 | 33/45 (CHP-212, hTERT-HPNE, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.613×** | -6.9 | 3e-10 | 30/45 (RPMI-7951, C32, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.675×** | -5.8 | 5e-07 | 29/45 (BT-474, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.710×** | -5.0 | 3e-05 | 25/45 (A549, NCI-H1792, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.788×** | -5.0 | 4e-05 | 24/45 (SK-MEL-2, A549, …) | rises with dose | composition shift; position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.574×** | -4.3 | 0.001 | 19/34 (BT-474, C32, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.817×** | -4.2 | 0.001 | 26/45 (SNU-423, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.749×** | -4.1 | 0.002 | 22/45 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.783×** | -3.6 | 0.012 | 26/46 (CFPAC-1, HS-578T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -3.5 | 0.017 | 17/45 (SK-MEL-2, NCI-H1573, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.635×** | -3.5 | 0.017 | 21/46 (HS-578T, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.799×** | -3.3 | 0.029 | 22/45 (H4, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.795×** | -3.3 | 0.033 | 18/45 (A549, LS 180, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **0.806×** | -3.1 | 0.058 | 17/45 (A549, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9045. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 248 | 3 | 6 (6 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.63× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 44.9 | 9 (3 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 7.43× (z +19.8) | — |
| [[A-172 (line)]] | wt | 241 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.547× (z -9.2) |
| [[LS 180 (line)]] | wt | 36.9 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 7.07× (z +16.9) | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 119 | 1 | 6 (6 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.63× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -15.3) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 70.0 | 3 | 4 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.37× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -9.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 151 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0669× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 186 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.467× (z -9.9) |
| [[SW1417 (line)]] | alt | 39.3 | 7 (2 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 6.20× (z +15.5) | — |
| [[AsPC-1 (line)]] | alt | 29.1 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.53× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 40.6 | 5 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 19.4× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 141 | 2 | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.52× (z +11.1) | [[Ponatinib (drug)]] 5 µM 0.250× (z -12.2) |
| [[HOP62 (line)]] | alt | 203 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 43.8 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 10.6× (z +19.0) | — |
| [[NCI-H1792 (line)]] | alt | 167 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -14.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 111 | 3 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.03× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 185 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0734× (z -25.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 100 | 4 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.56× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -8.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 98.1 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.359× (z -9.4) |
| [[HS-578T (line)]] | alt | 181 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 173 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -17.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 193 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -17.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 102 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 6.16× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 40.2 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.29× (z +19.8) | — |
| [[NCI-H1573 (line)]] | alt | 42.0 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 5.85× (z +13.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.308× (z -8.9) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 153 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.199× (z -14.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 115 | 1 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.99× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.116× (z -17.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 36.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 64.6 | 3 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.42× (z +11.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.329× (z -8.8) ⚠ toxic |
| [[SW 900 (line)]] | alt | 146 | 1 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.53× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 35.7 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.74× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -8.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 43.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.13× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 75.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -13.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 323 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 32.6 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 7.90× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 106 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 42.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.07× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 68.5 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.83× (z +13.3) | — |
| [[SNU-1 (line)]] | wt | 26.1 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 9.27× (z +10.8) | — |
| [[SW48 (line)]] | wt | 48.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.13× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 159 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H661 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0912× (z -8.6) ⚠ cell-cycle shift, explains ~81% of this change |
| [[SW 1271 (line)]] | alt | 65.5 | 0 | 1 | — | [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0782× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 23.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 24.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 200 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9045), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C9orf24]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 | STRING 566; ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[P4HA2]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[ABCB6]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PCYT1A]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[TANGO2]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[NQO2]] | +0.63 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[AAK1]] | +0.62 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[ZFAND2A]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[RELL2]] | +0.60 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[EPS15L1]] | +0.58 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[PSMD8]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[DNAJB2]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ATP2C1]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPEPLD]] | -0.61 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[PUM2]] | -0.59 | -0.33 / -0.62 | both halves | 1e-04 |  |
| [[TGFBR2]] | -0.58 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[HNRNPD]] | -0.55 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[SHROOM3]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[SLC12A2-DT]] | -0.52 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[RBMS2]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[PRPF4B]] | -0.52 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[ZFP36L2]] | -0.51 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[TBL1XR1]] | -0.51 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[PON2]] | -0.51 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[SORL1]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOXL2]] | B | LOXL2 activity raises FAM219A's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 2.53× lower at baseline in the lines without LOXL2 | 0.056 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[ZNF470]] | B | ZNF470 activity raises FAM219A's level | lines that do not express ZNF470 (18) vs lines expressing it (32) | 1.75× lower at baseline in the lines without ZNF470 | 0.070 | ⚠ within organs, on part of the lines; also absent: ZFP28, ZNF71, ZIM2-AS1 |
| [[PSMB5]] | B | PSMB5 activity lowers FAM219A's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TMEM255B]] | B | TMEM255B activity raises FAM219A's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 1.72× lower at baseline in the lines without TMEM255B | 0.090 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD39]] | C | FAM219A activity lowers ANKRD39's level | lines that do not express FAM219A (3) vs lines expressing it (47) | 1.67× higher at baseline in the lines without FAM219A | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SH3PXD2A, METRNL; maybe low, not absent; its own permutation p |
| [[SRSF10]] | C | FAM219A activity lowers SRSF10's level | lines that do not express FAM219A (3) vs lines expressing it (47) | 1.28× higher at baseline in the lines without FAM219A | 0.096 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SH3PXD2A, METRNL; maybe low, not absent |

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.5, -15.8); signed map (-40.1, 30.2). **Vector** length 135, 46.1% of its response variance represented; |z| ≥ 3 in 1,405 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +13.2 | +17.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +13.0 | +17.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +12.8 | +14.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +6.1 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.8 | +6.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.3 | +4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +2.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.2 | -11.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -5.4 | -7.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.3 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -4.4 | -6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.3 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -0.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 219 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:34,398,184-34,458,570 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA573M23.5, FLJ39031; previously C9orf25 |
| Matched by | ensembl_id |

UniProt [Q8IW50](https://www.uniprot.org/uniprotkb/Q8IW50) carries no function annotation.

**Summary**, from NCBI Gene [203259](https://www.ncbi.nlm.nih.gov/gene/203259):

> The protein encoded by this gene has homologs that have been identified in mouse, macaque, etc organisms. Multiple alternatively spliced transcript variants that encode different protein isoforms have been described for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:19920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19920) · Entrez [203259](https://www.ncbi.nlm.nih.gov/gene/203259) · UniProt [Q8IW50](https://www.uniprot.org/uniprotkb/Q8IW50) · Ensembl [ENSG00000164970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164970)

## Data

Gene col 9045: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9045); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9045, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9045]; `tensor/DDL_lfc|DDL_z.npy` [9045]; `embed/gene_vectors.npy` [9045]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9045 or target_col == 9045). Every well: [[FAM219A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM219A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
