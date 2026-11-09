---
symbol: "PAICS"
type: "gene"
col: 4859
ensembl_id: "ENSG00000128050"
name: "phosphoribosylaminoimidazole carboxylase and phosphoribosylaminoimidazolesuccinocarboxamide synthase"
location: "4q12"
module: 20
arm: "+"
pooled_cpm: 118.35
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PAICS

*phosphoribosylaminoimidazole carboxylase and phosphoribosylaminoimidazolesuccinocarboxamide synthase* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.80× (z +19.3, q 0e+00, up in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 1.73× (z +5.6, q 3e-06, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.452× (z -21.9, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKDC]] (+0.76, fdr 7e-06), [[IPO5]] (+0.74, fdr 7e-06), [[RPE]] (+0.73, fdr 7e-06); moves opposite to [[EIF1B]] (-0.69, fdr 7e-06), [[TERF2IP]] (-0.66, fdr 7e-06), [[CROCCP2-1]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAM216A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4859.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +19.3 | 0e+00 | 43/44 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.52×** | +18.0 | 0e+00 | 48/49 (A498, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.95×** | +12.0 | 6e-31 | 40/45 (LoVo, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +7.6 | 6e-12 | 42/48 (HT-29, AsPC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.73×** | +5.6 | 3e-06 | 41/48 (AsPC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.60×** | +4.8 | 2e-04 | 34/48 (AsPC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.59×** | +4.7 | 2e-04 | 31/48 (A498, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.7 | 0.017 | 19/38 (NCI-H2347, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.017 | 23/48 (A498, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.017 | 25/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.033 | 22/48 (AsPC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 1.19× | +3.2 | 0.059 | 22/50 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.12× | +3.2 | 0.069 | 6/48 (NCI-H1792, KATO III, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.12× | +3.1 | 0.079 | 7/49 (LS 180, HT-29, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4859.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.452×** | -21.9 | 0e+00 | 46/48 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.604×** | -7.2 | 2e-10 | 32/48 (MIA PaCa-2, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.700×** | -6.7 | 5e-09 | 30/48 (NCI-H23, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.744×** | -5.8 | 1e-06 | 28/48 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.757×** | -5.4 | 7e-06 | 26/48 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.769×** | -5.1 | 3e-05 | 29/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.653×** | -4.3 | 0.001 | 30/49 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.803×** | -4.1 | 0.003 | 24/47 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.812×** | -4.0 | 0.003 | 23/48 (SW 1088, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.812×** | -4.0 | 0.003 | 24/48 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 0.865× | -4.0 | 0.003 | 15/48 (A498, NCI-H2030, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.765×** | -3.8 | 0.007 | 26/48 (SW 1088, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.874× | -3.7 | 0.009 | 10/49 (A498, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -3.4 | 0.032 | 22/48 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.850× | -3.2 | 0.060 | 21/49 (RKO, SK-MEL-2, …) | top dose only |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.821×** | -3.0 | 0.086 | 18/49 (NCI-H23, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.744×** | -3.0 | 0.086 | 14/50 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.859× | -3.0 | 0.098 | 18/47 (SK-MEL-2, A498, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4859. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 105 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -15.8) |
| [[MIA PaCa-2 (line)]] | alt | 154 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -23.4) |
| [[RKO (line)]] | wt | 184 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -18.6) |
| [[SNU-1 (line)]] | wt | 187 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -33.2) |
| [[NCI-H23 (line)]] | alt | 215 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -25.5) |
| [[A498 (line)]] | wt | 109 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +17.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.635× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 64.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.31× (z +14.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -10.2) |
| [[Hs 766T (line)]] | wt | 96.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -9.6) |
| [[HT-29 (line)]] | alt | 77.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.25× (z +16.3) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 127 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.588× (z -10.0) |
| [[KATO III (line)]] | alt | 64.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.37× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -10.1) |
| [[LoVo (line)]] | wt | 98.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.45× (z +17.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 69.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.28× (z +13.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 98.3 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 134 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +16.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -19.5) |
| [[PANC-1 (line)]] | alt | 123 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -14.0) |
| [[SW 900 (line)]] | alt | 98.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.1) |
| [[SW1417 (line)]] | alt | 73.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -9.0) |
| [[A-427 (line)]] | wt | 140 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -34.2) |
| [[BT-474 (line)]] | alt | 103 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -16.3) |
| [[HOP62 (line)]] | alt | 117 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -14.7) |
| [[HS-578T (line)]] | alt | 97.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 97.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 96.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +13.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 242 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.80× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -14.7) |
| [[SK-MEL-2 (line)]] | alt | 134 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -13.2) |
| [[SNU-423 (line)]] | alt | 94.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +13.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 175 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +15.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -25.5) |
| [[A-172 (line)]] | wt | 62.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A549 (line)]] | wt | 102 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 139 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0919× (z -13.5) |
| [[HCT15 (line)]] | alt | 222 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -17.0) |
| [[HepG2_C3A (line)]] | wt | 86.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 84.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.18× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -17.6) |
| [[Panc 03.27 (line)]] | alt | 64.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 137 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.5) |
| [[C-33 A (line)]] | alt | 191 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.2) |
| [[C32 (line)]] | wt | 156 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 151 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -14.3) |
| [[CHP-212 (line)]] | wt | 156 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -15.4) |
| [[COLO 205 (line)]] | alt | 49.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[H4 (line)]] | wt | 140 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 123 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.6) |
| [[SW 1088 (line)]] | alt | 132 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.141× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4859), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | +0.76 | +0.71 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[IPO5]] | +0.74 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[RPE]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[LRPPRC]] | +0.71 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 | STRING 900 |
| [[RPSA]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[PPAT]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 | same gene group; pathway: Metabolism of nucleotides; STRING 999; ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[NUP205]] | +0.66 | +0.64 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[PFKM]] | +0.66 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[TXNDC5]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[SIGMAR1]] | +0.66 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[BPNT2]] | +0.66 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[EMC1]] | +0.65 | +0.55 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF1B]] | -0.69 | -0.61 / -0.73 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.66 | -0.64 / -0.67 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | -0.64 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[GABARAPL2]] | -0.64 | -0.54 / -0.74 | both halves | 1e-05 |  |
| [[IER5]] | -0.64 | -0.58 / -0.62 | both halves | 8e-06 |  |
| [[COX17]] | -0.63 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.63 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[TNRC6C]] | -0.63 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[ITSN2]] | -0.62 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[SYF2]] | -0.62 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[SAT2]] | -0.61 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[CHKB]] | -0.61 | -0.54 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM216A]] | B | FAM216A activity raises PAICS's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without FAM216A | 0.055 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.712). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.5, -31.3); signed map (-19.8, -44.6). **Vector** length 141, 50.5% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.7 | +7.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.9 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.9 | +4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.7 | +5.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +4.3 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +4.1 | +3.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -21.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.9 | -2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -7.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -4.3 | -1.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -4.3 | -3.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -4.1 | -4.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.9 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphoribosylaminoimidazole carboxylase and phosphoribosylaminoimidazolesuccinocarboxamide synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:56,435,741-56,464,578 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ADE2H1, AIRC; previously PAIS |
| Gene groups (HGNC) | Purinosome; Decarboxylases; Ligases |
| Hallmark sets | E2F_TARGETS |
| Reactome | 3 pathways, smallest: Purine ribonucleoside monophosphate biosynthesis; Nucleotide biosynthesis; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P22234](https://www.uniprot.org/uniprotkb/P22234) (Bifunctional phosphoribosylaminoimidazole carboxylase/phosphoribosylaminoimidazole succinocarboxamide synthetase):

> Bifunctional phosphoribosylaminoimidazole carboxylase and phosphoribosylaminoimidazole succinocarboxamide synthetase catalyzing two reactions of the de novo purine biosynthetic pathway.

**Summary**, from NCBI Gene [10606](https://www.ncbi.nlm.nih.gov/gene/10606):

> This gene encodes a bifunctional enzyme containing phosphoribosylaminoimidazole carboxylase activity in its N-terminal region and phosphoribosylaminoimidazole succinocarboxamide synthetase in its C-terminal region. It catalyzes steps 6 and 7 of purine biosynthesis. The gene is closely linked and divergently transcribed with a locus that encodes an enzyme in the same pathway, and transcription of the two genes is coordinately regulated. The human genome contains several pseudogenes of this gene. …

**Accessions** — [HGNC:8587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8587) · Entrez [10606](https://www.ncbi.nlm.nih.gov/gene/10606) · UniProt [P22234](https://www.uniprot.org/uniprotkb/P22234) · Ensembl [ENSG00000128050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128050)

## Data

Gene col 4859: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4859); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4859, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4859]; `tensor/DDL_lfc|DDL_z.npy` [4859]; `embed/gene_vectors.npy` [4859]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4859 or target_col == 4859). Every well: [[PAICS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAICS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
