---
symbol: "PNN"
type: "gene"
col: 2048
ensembl_id: "ENSG00000100941"
name: "pinin, desmosome associated protein"
location: "14q21.1"
module: 5
arm: "+"
pooled_cpm: 190.4
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PNN

*pinin, desmosome associated protein* — 14q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (24 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.15× (z +16.2, q 0e+00, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.89× (z +9.6, q 1e-19, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.775× (z -3.8, q 0.037, down in 38 of 49 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 0.833× (z -3.8, q 0.037, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[crizotinib (drug)]] 0.05 µM in 1 line (SW 1088 0.0728×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM25]] (+0.68, fdr 7e-06), [[EIF3A]] (+0.66, fdr 7e-06), [[DNAJC2]] (+0.52, fdr 4e-05); moves opposite to [[RRAGA]] (-0.52, fdr 1e-04), [[ATRAID]] (-0.48, fdr 3e-05), [[PPP1CA]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 24 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2048.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.15×** | +16.2 | 0e+00 | 45/48 (LoVo, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.58×** | +14.2 | 1e-43 | 48/49 (LoVo, COLO 205, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.32×** | +12.1 | 1e-31 | 41/44 (LoVo, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.40×** | +12.1 | 1e-31 | 45/45 (LoVo, NCI-H1573, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.89×** | +9.6 | 1e-19 | 48/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +9.2 | 4e-18 | 43/48 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +7.8 | 6e-13 | 41/48 (SNU-423, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +7.3 | 2e-11 | 46/48 (A498, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.62×** | +7.3 | 2e-11 | 45/48 (PANC-1, H4, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.60×** | +7.1 | 8e-11 | 45/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +7.0 | 2e-10 | 40/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.60×** | +6.8 | 4e-10 | 39/48 (A498, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.57×** | +6.8 | 6e-10 | 41/48 (Hs 766T, NCI-H1792, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +6.6 | 2e-09 | 45/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.56×** | +6.4 | 5e-09 | 42/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +5.2 | 5e-06 | 37/48 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.76×** | +4.5 | 2e-04 | 41/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.002 | 37/49 (SNU-423, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.65×** | +3.9 | 0.002 | 35/48 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.002 | 33/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.002 | 35/48 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.004 | 37/49 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.010 | 33/48 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.013 | 32/48 (A498, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.019 | 26/48 (CFPAC-1, AN3 CA, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.030 | 30/48 (SW 900, SHP-77, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2048.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[crizotinib (drug)]] 0.05 µM in 1 line (SW 1088 0.0728×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.775×** | -3.8 | 0.037 | 38/49 (J82, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.833×** | -3.8 | 0.037 | 26/48 (NCI-H23, A-427, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.780×** | -3.7 | 0.037 | 35/48 (NCI-H460, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2048. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 94.9 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +13.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.63× (z +12.4) | — |
| [[A498 (line)]] | wt | 137 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +18.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.51× (z +11.2) | — |
| [[H4 (line)]] | wt | 126 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +11.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.98× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 106 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LoVo (line)]] | wt | 217 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +19.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.90× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 158 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 128 | 7 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.69× (z +12.5) | — |
| [[HEC-1-A (line)]] | alt | 245 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +14.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 130 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +16.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 163 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +15.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LOX-IMVI (line)]] | wt | 192 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 273 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.17× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 213 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +13.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.54× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 182 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +18.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 123 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +15.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 207 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +15.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[C32 (line)]] | wt | 105 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +15.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.81× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 98.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 151 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +15.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 115 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +16.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +9.0) | — |
| [[J82 (line)]] | alt | 188 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW480 (line)]] | alt | 267 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.36× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 206 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.39× (z +10.3) | — |
| [[KATO III (line)]] | alt | 156 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[RKO (line)]] | wt | 225 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.23× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 255 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.49× (z +10.5) | — |
| [[A-172 (line)]] | wt | 101 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +15.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[AsPC-1 (line)]] | alt | 169 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +17.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[CFPAC-1 (line)]] | alt | 224 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.46× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 156 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HCT15 (line)]] | alt | 205 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H2030 (line)]] | alt | 233 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.36× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 278 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[Panc 03.27 (line)]] | alt | 267 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW48 (line)]] | wt | 290 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.37× (z +9.5) | — |
| [[A549 (line)]] | wt | 173 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +12.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[BT-474 (line)]] | alt | 364 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.21× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 332 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.24× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 146 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2347 (line)]] | alt | 206 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +11.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 142 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.61× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SNU-1 (line)]] | wt | 246 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +13.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW 1088 (line)]] | alt | 96.2 | 0 | 1 | — | [[crizotinib (drug)]] 0.05 µM 0.0728× (z -9.1) |
| [[SW1417 (line)]] | alt | 243 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 291 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 195 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 199 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2048), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM25]] | +0.68 | +0.75 / +0.61 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 812 |
| [[EIF3A]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[DNAJC2]] | +0.52 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[RBM28]] | +0.51 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[DDX46]] | +0.49 | +0.47 / +0.56 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 418 |
| [[TCERG1]] | +0.49 | +0.49 / +0.44 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 467 |
| [[GTPBP4]] | +0.49 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[ZRANB2]] | +0.48 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[NOM1]] | +0.48 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[BMS1P20]] | +0.46 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[FPGS]] | +0.45 | +0.39 / +0.37 | both halves | 8e-05 |  |
| [[NUDC]] | +0.45 | +0.50 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAGA]] | -0.52 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[ATRAID]] | -0.48 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[PPP1CA]] | -0.47 | -0.42 / -0.49 | both halves | 4e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TMEM179B]] | -0.46 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[PSENEN]] | -0.46 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[GRN]] | -0.45 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[CMC4]] | -0.45 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[SMPD1]] | -0.45 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[LIX1L]] | -0.45 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[HINT2]] | -0.44 | -0.18 / -0.46 | ⚠ not reproduced | 1e-03 |  |
| [[BLOC1S1]] | -0.44 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[MRPL40]] | -0.44 | -0.23 / -0.48 | both halves | 6e-04 |  |
| [[TNKS2]] | -0.44 | -0.31 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.294). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-24.8, -40.7); signed map (4.4, -43.8). **Vector** length 72.9, 27.5% of its response variance represented; |z| ≥ 3 in 1,403 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +6.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.5 | +9.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +2.6 | +1.3 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.3 | +0.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.4 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.3 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.9 | +7.3 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -2.4 | -1.4 |
|  | [[Canagliflozin (drug)]] 0.05 µM |  | -2.1 | -0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.1 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +1.7 |

## What is on record

|  |  |
|---|---|
| Name | pinin, desmosome associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.1 — chr14:39,175,183-39,183,220 (+) |
| Ensembl biotype | protein_coding |
| Also known as | memA |
| Hallmark sets | E2F_TARGETS |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H307](https://www.uniprot.org/uniprotkb/Q9H307) (Pinin):

> Transcriptional activator binding to the E-box 1 core sequence of the E-cadherin promoter gene; the core-binding sequence is 5'CAGGTG-3'. Capable of reversing CTBP1-mediated transcription repression. Auxiliary component of the splicing-dependent multiprotein exon junction complex (EJC) deposited at splice junction on mRNAs. The EJC is a dynamic structure consisting of core proteins and several peripheral nuclear and cytoplasmic associated factors that join the complex only transiently either …

**Summary**, from NCBI Gene [5411](https://www.ncbi.nlm.nih.gov/gene/5411):

> Enables RNA binding activity. Predicted to be involved in several processes, including mRNA splicing, via spliceosome; positive regulation of apoptotic process; and regulation of mRNA metabolic process. Predicted to act upstream of or within cell-cell adhesion. Located in exon-exon junction complex and nuclear speck. Part of catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9162](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9162) · Entrez [5411](https://www.ncbi.nlm.nih.gov/gene/5411) · UniProt [Q9H307](https://www.uniprot.org/uniprotkb/Q9H307) · Ensembl [ENSG00000100941](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100941)

## Data

Gene col 2048: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2048); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2048, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2048]; `tensor/DDL_lfc|DDL_z.npy` [2048]; `embed/gene_vectors.npy` [2048]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2048 or target_col == 2048). Every well: [[PNN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
