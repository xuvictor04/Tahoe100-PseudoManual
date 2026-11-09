---
symbol: "PDSS2"
type: "gene"
col: 8955
ensembl_id: "ENSG00000164494"
name: "decaprenyl diphosphate synthase subunit 2"
location: "6q21"
module: 207
arm: "+"
pooled_cpm: 139.34
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# PDSS2

*decaprenyl diphosphate synthase subunit 2* — 6q21

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 1.93×, NCI-H2030 1.63×; ⚠ cell-cycle shift, explains ~46% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 1.75×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 1.51×; ⚠ cell-cycle shift, explains ~19% of this change).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.405× (z -23.2, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.621× (z -12.2, q 4e-32, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF248]] (+0.61, fdr 1e-05), [[CNPY2]] (+0.58, fdr 3e-04), [[COG7]] (+0.58, fdr 1e-05); moves opposite to [[YWHAZ]] (-0.59, fdr 2e-05), [[EPPK1]] (-0.57, fdr 1e-05), [[ADAMTSL5]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 207]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8955.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 1.93×, NCI-H2030 1.63×; ⚠ cell-cycle shift, explains ~46% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 1.75×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 1.51×; ⚠ cell-cycle shift, explains ~19% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.10× | +3.4 | 0.25 | 11/48 (PANC-1, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.25 | 6/49 (SK-MEL-2, LoVo, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.13× | +3.0 | 0.35 | 14/49 (HepG2/C3A, A-427, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.12× | +3.0 | 0.35 | 9/48 (RKO, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 22 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8955.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.405×** | -23.2 | 0e+00 | 47/49 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.460×** | -19.1 | 0e+00 | 42/44 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.485×** | -16.6 | 0e+00 | 44/45 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.563×** | -14.2 | 3e-43 | 44/48 (A498, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.690×** | -13.4 | 4e-39 | 34/48 (SNU-423, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.621×** | -12.2 | 4e-32 | 44/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.664×** | -10.1 | 5e-22 | 37/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.701×** | -9.1 | 8e-18 | 34/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.703×** | -9.0 | 1e-17 | 40/48 (KATO III, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.703×** | -9.0 | 1e-17 | 34/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.710×** | -8.8 | 1e-16 | 37/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.715×** | -8.6 | 5e-16 | 36/48 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.797×** | -8.2 | 1e-14 | 32/48 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.743×** | -7.3 | 1e-11 | 36/47 (RKO, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.759×** | -7.1 | 6e-11 | 27/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.815×** | -5.2 | 5e-06 | 24/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.820×** | -5.1 | 1e-05 | 25/48 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.743×** | -3.9 | 0.003 | 22/49 (MIA PaCa-2, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.867× | -3.7 | 0.006 | 19/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.864× | -3.6 | 0.008 | 18/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.875× | -3.3 | 0.022 | 13/47 (CFPAC-1, RKO, …) | all doses, stronger at high dose |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.874× | -3.2 | 0.024 | 6/48 (KATO III, SNU-423, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.882× | -3.2 | 0.026 | 14/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.872× | -3.1 | 0.034 | 16/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.800×** | -2.9 | 0.056 | 10/48 (HOP62, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.922× | -2.9 | 0.058 | 4/49 (A-172, hTERT-HPNE, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 162 | 0 | 11 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -21.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.530× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 117 | 0 | 10 (9 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.319× (z -18.3) ⚠ toxic; cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.400× (z -15.2) |
| [[RPMI-7951 (line)]] | alt | 175 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.389× (z -12.2) |
| [[SW480 (line)]] | alt | 154 | 0 | 10 (9 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.328× (z -19.8) |
| [[C32 (line)]] | wt | 170 | 0 | 9 (7 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.337× (z -15.7) |
| [[HOP62 (line)]] | alt | 110 | 0 | 9 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.331× (z -17.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.509× (z -11.1) |
| [[SNU-423 (line)]] | alt | 178 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -22.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.344× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 156 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -21.5) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.342× (z -16.1) |
| [[SW 900 (line)]] | alt | 112 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -14.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.402× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 126 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -22.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[J82 (line)]] | alt | 106 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.555× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 113 | 1 (1 ⚠) | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.51× (z +9.0) ⚠ cell-cycle shift, explains ~19% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.514× (z -10.4) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.554× (z -9.2) |
| [[PANC-1 (line)]] | alt | 219 | 1 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.194× (z -26.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 134 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -15.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 105 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.225× (z -18.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.301× (z -15.4) |
| [[KATO III (line)]] | alt | 218 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -19.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 146 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +14.2) ⚠ cell-cycle shift, explains ~46% of this change | [[Dinaciclib (drug)]] 5 µM 0.381× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.630× (z -9.9) |
| [[A-172 (line)]] | wt | 77.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.463× (z -9.2) |
| [[COLO 205 (line)]] | alt | 114 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -11.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 128 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -16.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.380× (z -9.5) |
| [[HT-29 (line)]] | alt | 135 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.482× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 136 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +10.3) ⚠ cell-cycle shift, explains ~46% of this change | [[Dinaciclib (drug)]] 5 µM 0.364× (z -14.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 152 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -13.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 87.6 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.373× (z -13.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.473× (z -10.2) |
| [[AN3 CA (line)]] | alt | 202 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.310× (z -9.7) |
| [[C-33 A (line)]] | alt | 164 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.514× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 97.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.358× (z -13.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 147 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -19.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 108 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.355× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 137 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -14.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[Panc 03.27 (line)]] | alt | 124 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -20.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 132 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0873× (z -29.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 96.4 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.127× (z -11.7) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 132 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0792× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.294× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -12.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[Hs 766T (line)]] | wt | 112 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -11.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -16.3) ⚠ cell-cycle shift, explains ~19% of this change |
| [[LS 180 (line)]] | wt | 200 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 190 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -23.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 141 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -14.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -21.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 136 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.391× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 176 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -14.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 203 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 197 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF248]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[CNPY2]] | +0.58 | +0.28 / +0.66 | both halves | 3e-04 |  |
| [[COG7]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ATP5PF]] | +0.58 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[KLHDC10]] | +0.58 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[CHCHD1]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PDHX]] | +0.57 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[INTS9]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[PMS2P4-1]] | +0.56 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ELP4]] | +0.55 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[MED4]] | +0.55 | +0.32 / +0.60 | both halves | 1e-04 |  |
| [[COQ4]] | +0.55 | +0.46 / +0.57 | both halves | 2e-05 | pathway: Metabolism of cofactors; STRING 874 |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAZ]] | -0.59 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[EPPK1]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ADAMTSL5]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[JUNB]] | -0.55 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[WDR1]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[CSRP1]] | -0.54 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[MYH9]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[R3HDM4]] | -0.53 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[C15orf39]] | -0.52 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[RAPH1]] | -0.52 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[CSRNP1]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ANXA5]] | -0.51 | -0.39 / -0.54 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **+** arm (projection on the module's main direction 0.584). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-24.1, 28.2); signed map (-20.5, 1.6). **Vector** length 104, 31.9% of its response variance represented; |z| ≥ 3 in 1,291 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.4 | +3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +0.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.9 | +3.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +0.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +0.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.9 | +0.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | +0.7 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | +1.8 | -0.0 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.8 | -0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.1 | -8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.8 | -16.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.5 | -2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | -19.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | -5.3 | -10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -12.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.5 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | decaprenyl diphosphate synthase subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:107,152,562-107,459,564 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA59I9.3, COQ1B; previously C6orf210 |
| Reactome | 3 pathways, smallest: Ubiquinol biosynthesis; Metabolism of cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YH6](https://www.uniprot.org/uniprotkb/Q86YH6) (All trans-polyprenyl-diphosphate synthase PDSS2):

> Heterotetrameric enzyme that catalyzes the condensation of farnesyl diphosphate (FPP), which acts as a primer, and isopentenyl diphosphate (IPP) to produce prenyl diphosphates of varying chain lengths and participates in the determination of the side chain of ubiquinone. Supplies nona and decaprenyl diphosphate, the precursors for the side chain of the isoprenoid quinones ubiquinone-9 (Q9) and ubiquinone-10 (Q10) respectively. The enzyme adds isopentenyl diphosphate molecules sequentially to …

**Summary**, from NCBI Gene [57107](https://www.ncbi.nlm.nih.gov/gene/57107):

> The protein encoded by this gene is an enzyme that synthesizes the prenyl side-chain of coenzyme Q, or ubiquinone, one of the key elements in the respiratory chain. The gene product catalyzes the formation of all trans-polyprenyl pyrophosphates from isopentyl diphosphate in the assembly of polyisoprenoid side chains, the first step in coenzyme Q biosynthesis. Defects in this gene are a cause of coenzyme Q10 deficiency.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:23041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23041) · Entrez [57107](https://www.ncbi.nlm.nih.gov/gene/57107) · UniProt [Q86YH6](https://www.uniprot.org/uniprotkb/Q86YH6) · Ensembl [ENSG00000164494](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164494)

## Data

Gene col 8955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8955); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8955]; `tensor/DDL_lfc|DDL_z.npy` [8955]; `embed/gene_vectors.npy` [8955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8955 or target_col == 8955). Every well: [[PDSS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDSS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
