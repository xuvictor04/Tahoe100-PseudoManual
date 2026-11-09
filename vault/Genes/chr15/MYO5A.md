---
symbol: "MYO5A"
type: "gene"
col: 12412
ensembl_id: "ENSG00000197535"
name: "myosin VA"
location: "15q21.2"
module: 78
arm: "+"
pooled_cpm: 106.54
n_lines_expressing: 44
n_dd_up: 6
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 11
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# MYO5A

*myosin VA* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.75× (z +15.2, q 0e+00, up in 32 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.28× (z +7.1, q 2e-10, up in 22 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (PANC-1 2.20×, C32 2.20×, RPMI-7951 2.60×, SW480 1.84×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (PANC-1 2.01×, SW480 1.84×, C32 1.96×, HOP62 2.05×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 2.49×, NCI-H460 1.52×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CFPAC-1 1.97×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 1.88×).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.636× (z -18.3, q 0e+00, down in 32 of 42 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.754× (z -11.3, q 1e-27, down in 25 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (SNU-1 0.415×, NCI-H2030 0.531×, NCI-H1573 0.442×, PANC-1 0.621×, …); [[Homoharringtonine (drug)]] 5 µM in 9 lines (HOP62 0.339×, AN3 CA 0.189×, J82 0.384×, NCI-H1573 0.347×, …; ⚠ cell-cycle shift, explains ~27% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 4 lines (J82 0.446×, NCI-H460 0.538×, NCI-H1792 0.467×, HEC-1-A 0.491×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RALB]] (+0.62, fdr 7e-06), [[MAP1B]] (+0.62, fdr 7e-06), [[ZDHHC21]] (+0.60, fdr 1e-05); moves opposite to [[EFNA1]] (-0.53, fdr 2e-05), [[RBM15]] (-0.52, fdr 7e-05), [[CSTF1]] (-0.47, fdr 3e-04).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BVES]] → it (grade B ⚠); 11 go from it, the strongest it → [[DYNC1H1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12412.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (PANC-1 2.20×, C32 2.20×, RPMI-7951 2.60×, SW480 1.84×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (PANC-1 2.01×, SW480 1.84×, C32 1.96×, HOP62 2.05×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 2.49×, NCI-H460 1.52×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CFPAC-1 1.97×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 1.88×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +15.2 | 0e+00 | 32/39 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +13.2 | 1e-37 | 31/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +7.1 | 2e-10 | 22/41 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +5.9 | 5e-07 | 23/41 (RPMI-7951, C32, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +5.9 | 5e-07 | 22/42 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.23×** | +5.1 | 4e-05 | 20/40 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +4.9 | 7e-05 | 7/42 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.16× | +4.0 | 0.004 | 17/41 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.14× | +3.8 | 0.008 | 14/43 (NCI-H460, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.09× | +3.5 | 0.025 | 15/42 (SW1417, BT-474, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.5 | 0.025 | 10/43 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.13× | +3.5 | 0.025 | 11/42 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.13× | +3.4 | 0.028 | 14/42 (SW480, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 20 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12412.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (SNU-1 0.415×, NCI-H2030 0.531×, NCI-H1573 0.442×, PANC-1 0.621×, …); [[Homoharringtonine (drug)]] 5 µM in 9 lines (HOP62 0.339×, AN3 CA 0.189×, J82 0.384×, NCI-H1573 0.347×, …; ⚠ cell-cycle shift, explains ~27% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 4 lines (J82 0.446×, NCI-H460 0.538×, NCI-H1792 0.467×, HEC-1-A 0.491×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.636×** | -18.3 | 0e+00 | 32/42 (HOP62, AN3 CA, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.598×** | -14.6 | 0e+00 | 31/42 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.641×** | -12.7 | 2e-34 | 28/42 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.754×** | -11.3 | 1e-27 | 25/43 (SNU-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.677×** | -11.1 | 1e-26 | 31/42 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.719×** | -9.4 | 5e-19 | 26/42 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.770×** | -7.4 | 9e-12 | 22/42 (HS-578T, SNU-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.808×** | -6.1 | 1e-07 | 23/42 (HEC-1-A, C32, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.801×** | -6.0 | 2e-07 | 20/41 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.823×** | -5.5 | 2e-06 | 20/41 (NCI-H460, SW 1271, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.815×** | -5.5 | 2e-06 | 21/41 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.835× | -4.8 | 5e-05 | 20/42 (NCI-H1573, A-172, …) | top dose only | composition shift |
| [[Sulfatinib (drug)]] 5 µM |  | 0.835× | -4.8 | 5e-05 | 18/43 (J82, NCI-H2030, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | 0.843× | -4.8 | 5e-05 | 19/42 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.847× | -4.7 | 9e-05 | 16/42 (HS-578T, C32, …) | two highest doses |  |
| [[Arbutin (drug)]] 5 µM |  | 0.882× | -3.4 | 0.020 | 2/42 (NCI-H1573, NCI-H23) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12412. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 87.4 | 1 | 9 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.52× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.317× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.538× (z -10.5) |
| [[C32 (line)]] | wt | 371 | 5 (3 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.20× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 1.88× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -11.1) |
| [[SNU-1 (line)]] | wt | 334 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 65.7 | 1 (1 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.92× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -12.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 98.1 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -16.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -12.7) |
| [[J82 (line)]] | alt | 100.0 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.446× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 145 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -12.0) |
| [[SW480 (line)]] | alt | 97.1 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.84× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.58× (z +8.8) | — |
| [[A-172 (line)]] | wt | 132 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -16.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HS-578T (line)]] | alt | 151 | 1 (1 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.06× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.333× (z -15.1) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -11.7) |
| [[PANC-1 (line)]] | alt | 159 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.20× (z +13.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -12.0) |
| [[A549 (line)]] | wt | 209 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -16.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 85.7 | 3 (1 ⚠) | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.97× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -10.7) |
| [[HOP62 (line)]] | alt | 119 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -21.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 124 | 1 (1 ⚠) | 3 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.57× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -13.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 185 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -20.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.366× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 174 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.60× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -13.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 68.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +17.6) | — |
| [[Hs 766T (line)]] | wt | 87.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 210 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -14.2) |
| [[SNU-423 (line)]] | alt | 92.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -13.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -9.1) ⚠ cell-cycle shift, explains ~16% of this change |
| [[LOX-IMVI (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.591× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 80.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -10.0) |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.102× (z -8.7) |
| [[SW 1271 (line)]] | alt | 88.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0909× (z -8.9) |
| [[SW 900 (line)]] | alt | 123 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 76.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -10.3) |
| [[SW48 (line)]] | wt | 81.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.346× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 91.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 117 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.6 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.34 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.58 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 175 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 146 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12412), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALB]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MAP1B]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ZDHHC21]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[DTD1]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CAPN2]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[DYNC1I2]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[RCAN3]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[MSN]] | +0.56 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[ATP13A2]] | +0.55 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[DYNLT3]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TMTC3]] | +0.54 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[IQGAP1]] | +0.53 | +0.50 / +0.56 | both halves | 1e-05 | STRING 416 |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA1]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[RBM15]] | -0.52 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[CSTF1]] | -0.47 | -0.29 / -0.57 | both halves | 3e-04 |  |
| [[MRPL23]] | -0.47 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[SETDB1]] | -0.46 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[TGIF2]] | -0.45 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[GPRC5C]] | -0.45 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[CEBPD]] | -0.45 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[RBX1]] | -0.45 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[SCAMP3]] | -0.45 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[POLR1H]] | -0.45 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[DPM3]] | -0.44 | -0.25 / -0.57 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BVES]] | B | BVES activity raises MYO5A's level | lines that do not express BVES (19) vs lines expressing it (31) | 2.17× lower at baseline in the lines without BVES | 0.083 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[TMOD2]] | C | TMOD2 activity raises MYO5A's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 5.93× lower at baseline in the lines without TMOD2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent; co-absent with the target |
| [[TTC7B]] | C | TTC7B activity raises MYO5A's level | lines that do not express TTC7B (9) vs lines expressing it (41) | 3.67× lower at baseline in the lines without TTC7B | 0.053 | ⚠ within organs, on part of the lines; also absent: SYNGR1, HDGFL3, HLTF; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC1H1]] | B | MYO5A activity raises DYNC1H1's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without MYO5A | 0.022 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[STX2]] | B | MYO5A activity raises STX2's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 2.85× lower at baseline in the lines without MYO5A | 0.036 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[EXOC5]] | B | MYO5A activity raises EXOC5's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 1.50× lower at baseline in the lines without MYO5A | 0.040 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[ANXA6]] | B | MYO5A activity raises ANXA6's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 4.01× lower at baseline in the lines without MYO5A | 0.040 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[DCTN1]] | B | MYO5A activity raises DCTN1's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without MYO5A | 0.060 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[UBE2Q2P1]] | B | MYO5A activity raises UBE2Q2P1's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 2.30× lower at baseline in the lines without MYO5A | 0.065 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[TGIF2]] | B | MYO5A activity raises TGIF2's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without MYO5A | 0.065 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[MAML1]] | B | MYO5A activity raises MAML1's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without MYO5A | 0.086 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[SPTBN1]] | B | MYO5A activity lowers SPTBN1's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 1.82× higher at baseline in the lines without MYO5A | 0.089 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[FYTTD1]] | B | MYO5A activity raises FYTTD1's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 1.17× lower at baseline in the lines without MYO5A | 0.095 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[TMOD2]] | C | MYO5A activity raises TMOD2's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 2.99× lower at baseline in the lines without MYO5A | 0.012 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2; co-absent with the target |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.438). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.9, 42.0); signed map (-8.9, 23.6). **Vector** length 125, 36.3% of its response variance represented; |z| ≥ 3 in 1,116 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +13.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.1 | +2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.4 | +4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.3 | +4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.0 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +1.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.5 | -14.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.8 | -11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.8 | -18.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.9 | -12.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | -3.3 | -4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -2.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.5 | -2.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.4 | -1.5 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.4 | -4.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | myosin VA |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:52,307,281-52,529,132 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MYO5, GS1, MYR12; previously MYH12 |
| Gene groups (HGNC) | Myosin heavy chains, class V |
| Reactome | 16 pathways, smallest: Insulin processing; Regulation of MITF-M-dependent genes involved in pigmentation; FCGR3A-mediated phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4I1](https://www.uniprot.org/uniprotkb/Q9Y4I1) (Unconventional myosin-Va):

> Processive actin-based motor that can move in large steps approximating the 36-nm pseudo-repeat of the actin filament. Can hydrolyze ATP in the presence of actin, which is essential for its function as a motor protein. Involved in melanosome transport. Also mediates the transport of vesicles to the plasma membrane (By similarity). May also be required for some polarization process involved in dendrite formation (By similarity).

**Summary**, from NCBI Gene [4644](https://www.ncbi.nlm.nih.gov/gene/4644):

> This gene is one of three myosin V heavy-chain genes, belonging to the myosin gene superfamily. Myosin V is a class of actin-based motor proteins involved in cytoplasmic vesicle transport and anchorage, spindle-pole alignment and mRNA translocation. The protein encoded by this gene is abundant in melanocytes and nerve cells. Mutations in this gene cause Griscelli syndrome type-1 (GS1) and neuroectodermal melanolysosomal disease, or Elejalde disease. [provided by RefSeq, Sep 2023]

**Accessions** — [HGNC:7602](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7602) · Entrez [4644](https://www.ncbi.nlm.nih.gov/gene/4644) · UniProt [Q9Y4I1](https://www.uniprot.org/uniprotkb/Q9Y4I1) · Ensembl [ENSG00000197535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197535)

## Data

Gene col 12412: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12412); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12412, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12412]; `tensor/DDL_lfc|DDL_z.npy` [12412]; `embed/gene_vectors.npy` [12412]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12412 or target_col == 12412). Every well: [[MYO5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
