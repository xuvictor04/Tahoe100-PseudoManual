---
symbol: "AP3D1"
type: "gene"
col: 768
ensembl_id: "ENSG00000065000"
name: "adaptor related protein complex 3 subunit delta 1"
location: "19p13.3"
module: 52
arm: "+"
pooled_cpm: 108.19
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# AP3D1

*adaptor related protein complex 3 subunit delta 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +17.0, q 0e+00, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.77× (z +11.3, q 1e-27, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.835× (z -5.1, q 2e-04, down in 22 of 48 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.813× (z -4.1, q 0.007, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HS-578T 0.510×; ⚠ cell-cycle shift, explains ~0% of this change); [[Thymopentin (drug)]] 5 µM in 1 line (SW 1088 0.101×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.458×; ⚠ toxic; cell-cycle shift, explains ~29% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SNU-1 0.350×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.371×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA3]] (+0.63, fdr 2e-05), [[CREB3]] (+0.61, fdr 2e-04), [[UVSSA]] (+0.59, fdr 1e-05); moves opposite to [[POU2F1]] (-0.57, fdr 2e-04), [[ZNRF2P1]] (-0.55, fdr 2e-05), [[HINT1]] (-0.52, fdr 3e-04).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 768.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.83×** | +17.0 | 0e+00 | 44/48 (NCI-H460, SNU-423, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +15.0 | 0e+00 | 42/44 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +12.9 | 1e-35 | 47/49 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +11.3 | 1e-27 | 40/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +9.4 | 5e-19 | 38/45 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.32×** | +5.4 | 8e-06 | 29/48 (RKO, PANC-1, …) | top dose only | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.29×** | +5.1 | 2e-05 | 27/48 (A-172, SNU-423, …) | two highest doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.007 | 27/48 (LoVo, SW480, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.8 | 0.009 | 22/48 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.014 | 20/48 (HEC-1-A, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.023 | 26/48 (SW480, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.026 | 17/49 (A-172, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | 1.18× | +3.3 | 0.044 | 19/48 (SHP-77, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.16× | +3.0 | 0.10 | 19/48 (SHP-77, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 768.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HS-578T 0.510×; ⚠ cell-cycle shift, explains ~0% of this change); [[Thymopentin (drug)]] 5 µM in 1 line (SW 1088 0.101×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.458×; ⚠ toxic; cell-cycle shift, explains ~29% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (SNU-1 0.350×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.371×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.835× | -5.1 | 2e-04 | 22/48 (J82, A498, …) | top dose only | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.806×** | -4.3 | 0.005 | 23/48 (HT-29, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.813×** | -4.1 | 0.007 | 29/48 (SNU-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -3.4 | 0.094 | 21/48 (HS-578T, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.3 | 0.095 | 19/48 (HS-578T, SW480, …) | rises with dose | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | 0.845× | -3.2 | 0.12 | 17/49 (HepG2/C3A, A-427, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.899× | -3.0 | 0.21 | 5/48 (SW 900, SHP-77, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 768. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 165 | 5 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +14.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.02× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.510× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 164 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +19.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 85.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +16.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 88.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 151 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +16.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +12.8) | — |
| [[NCI-H460 (line)]] | wt | 73.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +26.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.05× (z +17.6) | — |
| [[PANC-1 (line)]] | alt | 99.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +18.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 109 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +23.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HEC-1-A (line)]] | alt | 98.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.30× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 105 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +13.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.458× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 121 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +15.6) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H2347 (line)]] | alt | 93.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +10.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 73.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +15.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 117 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +12.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 165 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +11.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 74.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.9) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[C32 (line)]] | wt | 79.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.57× (z +12.3) | — |
| [[H4 (line)]] | wt | 137 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +12.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.17× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 87.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +9.5) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.371× (z -8.5) |
| [[Hs 766T (line)]] | wt | 82.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.2) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HT-29 (line)]] | alt | 109 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.12× (z +8.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.473× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 83.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +10.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 108 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +16.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.01× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 110 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 76.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +8.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.350× (z -8.8) |
| [[SW 1088 (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Thymopentin (drug)]] 5 µM 0.101× (z -8.9) |
| [[SW480 (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +11.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 148 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +13.7) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 97.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +9.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 58.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.9) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HCT15 (line)]] | alt | 169 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 123 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[J82 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[KATO III (line)]] | alt | 85.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.0) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[LoVo (line)]] | wt | 143 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.98× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 148 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +18.0) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[Panc 03.27 (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW 900 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.20× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 94.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 768), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA3]] | +0.63 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[CREB3]] | +0.61 | +0.76 / +0.30 | both halves | 2e-04 |  |
| [[UVSSA]] | +0.59 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[CEP63]] | +0.58 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[ASCC2]] | +0.56 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[FAM114A2]] | +0.56 | +0.66 / +0.31 | both halves | 2e-04 |  |
| [[SUPT5H]] | +0.56 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[GOLGB1]] | +0.55 | +0.68 / +0.39 | both halves | 5e-05 |  |
| [[ARL1]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[SART1]] | +0.54 | +0.58 / +0.37 | both halves | 8e-05 |  |
| [[SRP72]] | +0.54 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[TAF1]] | +0.54 | +0.59 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POU2F1]] | -0.57 | -0.69 / -0.32 | both halves | 2e-04 |  |
| [[ZNRF2P1]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[HINT1]] | -0.52 | -0.69 / -0.28 | both halves | 3e-04 |  |
| [[NAXE]] | -0.52 | -0.68 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |
| [[C1orf216]] | -0.49 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[PDS5B]] | -0.49 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[FANCL]] | -0.48 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ZNRF2P2]] | -0.48 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[ZNF738]] | -0.47 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[AMD1]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[NDUFB2]] | -0.47 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[TMEM98]] | -0.47 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[CMC1]] | -0.46 | -0.38 / -0.52 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.476). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-13.8, -53.1); signed map (-6.7, -21.7). **Vector** length 115, 34.8% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +11.1 | +17.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +15.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.3 | +5.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +3.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.5 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.2 | +2.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | -6.6 | -1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | -4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -6.0 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.9 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 3 subunit delta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,100,988-2,164,468 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADTD |
| Gene groups (HGNC) | Clathrin/coatomer adaptor, adaptin-like, N-terminal domain containing; Adaptor related protein complex 3 |
| Matched by | ensembl_id |

**Function**, from UniProt [O14617](https://www.uniprot.org/uniprotkb/O14617) (AP-3 complex subunit delta-1):

> Part of the AP-3 complex, an adaptor-related complex which is not clathrin-associated. The complex is associated with the Golgi region as well as more peripheral structures. It facilitates the budding of vesicles from the Golgi membrane and may be directly involved in trafficking to lysosomes. Involved in process of CD8+ T-cell and NK cell degranulation. In concert with the BLOC-1 complex, AP-3 is required to target cargos into vesicles assembled at cell bodies for delivery into neurites and …

**Summary**, from NCBI Gene [8943](https://www.ncbi.nlm.nih.gov/gene/8943):

> The protein encoded by this gene is a subunit of the AP3 adaptor-like complex, which is not clathrin-associated, but is associated with the golgi region, as well as more peripheral structures. The AP-3 complex facilitates the budding of vesicles from the golgi membrane, and may be directly involved in trafficking to lysosomes. This subunit is implicated in intracellular biogenesis and trafficking of pigment granules, and possibly platelet dense granules and neurotransmitter vesicles. Defects in …

**Accessions** — [HGNC:568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:568) · Entrez [8943](https://www.ncbi.nlm.nih.gov/gene/8943) · UniProt [O14617](https://www.uniprot.org/uniprotkb/O14617) · Ensembl [ENSG00000065000](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065000)

## Data

Gene col 768: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 768); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 768, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 768]; `tensor/DDL_lfc|DDL_z.npy` [768]; `embed/gene_vectors.npy` [768]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 768 or target_col == 768). Every well: [[AP3D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP3D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
