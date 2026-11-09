---
symbol: "NONO"
type: "gene"
col: 7154
ensembl_id: "ENSG00000147140"
name: "non-POU domain containing octamer binding"
location: "Xq13.1"
module: 25
arm: "+"
pooled_cpm: 136.48
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# NONO

*non-POU domain containing octamer binding* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.31× (z +17.8, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.56× (z +9.4, q 9e-19, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.808× (z -6.4, q 1e-07, down in 27 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (NCI-H460 0.491×, LoVo 0.493×, SW480 0.547×, CHP-212 0.304×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.472×, SW480 0.655×; ⚠ cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.196×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.562×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (SW 1088 0.0877×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF4H]] (+0.82, fdr 7e-06), [[LIN7C]] (+0.77, fdr 7e-06), [[CAPRIN1]] (+0.77, fdr 7e-06); moves opposite to [[SNHG9]] (-0.70, fdr 1e-05), [[DNLZ]] (-0.68, fdr 1e-05), [[ADPRS]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7154.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +17.8 | 0e+00 | 48/49 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +17.6 | 0e+00 | 44/44 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +15.1 | 0e+00 | 44/45 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +9.4 | 9e-19 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +8.0 | 2e-13 | 42/47 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +6.8 | 9e-10 | 36/48 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +5.5 | 3e-06 | 31/48 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **1.29×** | +5.4 | 5e-06 | 34/48 (NCI-H460, A498, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +5.2 | 1e-05 | 35/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +5.1 | 2e-05 | 32/48 (A498, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +4.9 | 6e-05 | 36/49 (PANC-1, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.26×** | +4.6 | 2e-04 | 23/48 (PANC-1, A498, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.24×** | +4.6 | 2e-04 | 28/48 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 8e-04 | 22/48 (SNU-423, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.21×** | +4.0 | 0.002 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.004 | 23/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Malotilate (drug)]] 0.05 µM |  | 1.19× | +3.8 | 0.005 | 20/48 (HOP62, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Oxaliplatin (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.005 | 26/48 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.007 | 26/48 (PANC-1, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 0.05 µM |  | 1.20× | +3.5 | 0.011 | 18/48 (PANC-1, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Cyclosporin A (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.059 | 11/48 (HOP62, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.060 | 12/47 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses |  |
| [[Pimozide (drug)]] 5 µM |  | 1.15× | +2.9 | 0.080 | 5/48 (A-427, SW480, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7154.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 10 lines (NCI-H460 0.491×, LoVo 0.493×, SW480 0.547×, CHP-212 0.304×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.472×, SW480 0.655×; ⚠ cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.196×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.562×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (SW 1088 0.0877×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.808×** | -6.4 | 1e-07 | 27/49 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.863× | -4.4 | 0.003 | 7/48 (SK-MEL-2, A-427, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -3.9 | 0.019 | 0/50 | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.882× | -3.7 | 0.028 | 7/48 (NCI-H460, RKO, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.789×** | -3.6 | 0.040 | 25/48 (SHP-77, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.855× | -3.3 | 0.089 | 10/49 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.900× | -3.1 | 0.14 | 16/48 (A-427, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7154. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 181 | 7 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +17.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -15.6) |
| [[SW480 (line)]] | alt | 261 | 4 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.98× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -12.4) |
| [[LoVo (line)]] | wt | 103 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -13.5) |
| [[LS 180 (line)]] | wt | 110 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -9.8) |
| [[KATO III (line)]] | alt | 155 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 184 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +14.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 79.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 137 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +17.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +12.3) | — |
| [[A-172 (line)]] | wt | 110 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +12.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 115 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +17.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 148 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +14.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 116 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 107 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 109 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.21× (z +10.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.646× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 110 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +9.3) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.196× (z -16.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 143 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +13.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 121 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +12.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 75.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +12.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 121 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +13.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 144 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 123 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 170 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 247 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +15.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 143 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +11.4) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.562× (z -10.3) |
| [[C-33 A (line)]] | alt | 148 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +9.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -10.7) |
| [[C32 (line)]] | wt | 100 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.61× (z +10.3) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 114 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +11.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -9.9) |
| [[HCT15 (line)]] | alt | 147 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +8.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -10.3) |
| [[J82 (line)]] | alt | 154 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 75.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 89.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.61× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 165 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +11.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 117 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +13.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 163 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +10.1) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -12.1) |
| [[COLO 205 (line)]] | alt | 97.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +10.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 100 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 109 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0877× (z -9.7) |
| [[SW 900 (line)]] | alt | 82.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 146 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 156 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 148 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7154), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4H]] | +0.82 | +0.76 / +0.84 | both halves | 7e-06 | same gene group; STRING 403 |
| [[LIN7C]] | +0.77 | +0.60 / +0.84 | both halves | 7e-06 |  |
| [[CAPRIN1]] | +0.77 | +0.70 / +0.81 | both halves | 7e-06 | STRING 483 |
| [[IPO5]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.73 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[HUWE1]] | +0.73 | +0.67 / +0.78 | both halves | 7e-06 | STRING 424 |
| [[DHFR]] | +0.73 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[PFKM]] | +0.73 | +0.67 / +0.69 | both halves | 7e-06 | same gene group |
| [[EEF1A1]] | +0.72 | +0.73 / +0.76 | both halves | 7e-06 | STRING 487 |
| [[OCRL]] | +0.72 | +0.47 / +0.79 | both halves | 2e-05 |  |
| [[DCTN1]] | +0.72 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[PRELID3B]] | +0.70 | +0.51 / +0.79 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG9]] | -0.70 | -0.50 / -0.78 | both halves | 1e-05 |  |
| [[DNLZ]] | -0.68 | -0.49 / -0.71 | both halves | 1e-05 |  |
| [[ADPRS]] | -0.66 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[ING2]] | -0.66 | -0.47 / -0.71 | both halves | 2e-05 |  |
| [[ZMYM5]] | -0.65 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[C1orf122]] | -0.64 | -0.38 / -0.75 | both halves | 6e-05 |  |
| [[ZBTB7A]] | -0.64 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.64 | -0.44 / -0.73 | both halves | 3e-05 |  |
| [[SMIM27]] | -0.63 | -0.42 / -0.70 | both halves | 4e-05 |  |
| [[RPL36AL]] ⚠ | -0.63 | -0.43 / -0.75 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LINC00685]] | -0.63 | -0.51 / -0.70 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.63 | -0.52 / -0.69 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DCTN6-DT]] | -0.63 | -0.49 / -0.72 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.62 | -0.52 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.3, -23.3); signed map (-19.9, -36.9). **Vector** length 121, 37.6% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +17.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | +17.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +15.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.3 | +1.7 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +3.1 | +1.9 |
|  | [[Erlotinib (drug)]] 5 µM |  | +3.0 | +1.9 |
|  | [[Artesunate (drug)]] 0.05 µM |  | +2.9 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.8 | -2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.7 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +1.3 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -3.3 | -0.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.3 | -2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.3 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | non-POU domain containing octamer binding |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:71,254,814-71,301,522 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p54(NRB), NRB54, NMT55, P54NRB, P54, PPP1R114 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15233](https://www.uniprot.org/uniprotkb/Q15233) (Non-POU domain-containing octamer-binding protein):

> DNA- and RNA binding protein, involved in several nuclear processes. Binds the conventional octamer sequence in double-stranded DNA. Also binds single-stranded DNA and RNA at a site independent of the duplex site. Involved in pre-mRNA splicing, probably as a heterodimer with SFPQ. Interacts with U5 snRNA, probably by binding to a purine-rich sequence located on the 3' side of U5 snRNA stem 1b. Together with PSPC1, required for the formation of nuclear paraspeckles. The SFPQ-NONO heteromer …

**Summary**, from NCBI Gene [4841](https://www.ncbi.nlm.nih.gov/gene/4841):

> This gene encodes an RNA-binding protein which plays various roles in the nucleus, including transcriptional regulation and RNA splicing. A rearrangement between this gene and the transcription factor E3 gene has been observed in papillary renal cell carcinoma. Alternatively spliced transcript variants have been described. Pseudogenes exist on Chromosomes 2 and 16. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:7871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7871) · Entrez [4841](https://www.ncbi.nlm.nih.gov/gene/4841) · UniProt [Q15233](https://www.uniprot.org/uniprotkb/Q15233) · Ensembl [ENSG00000147140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147140)

## Data

Gene col 7154: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7154); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7154, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7154]; `tensor/DDL_lfc|DDL_z.npy` [7154]; `embed/gene_vectors.npy` [7154]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7154 or target_col == 7154). Every well: [[NONO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NONO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
