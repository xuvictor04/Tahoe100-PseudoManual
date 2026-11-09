---
symbol: "DHX36"
type: "gene"
col: 10548
ensembl_id: "ENSG00000174953"
name: "DEAH-box helicase 36"
location: "3q25.2"
module: 12
arm: "+"
pooled_cpm: 174.64
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# DHX36

*DEAH-box helicase 36* — 3q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.43× (z +31.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.584× (z -12.5, q 2e-33, down in 39 of 45 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A549 0.201×, NCI-H1573 0.281×, HEC-1-A 0.285×, NCI-H23 0.338×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (SK-MEL-2 0.333×, HEC-1-A 0.346×, KATO III 0.440×, NCI-H2347 0.467×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.402×, LOX-IMVI 0.356×, H4 0.352×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL46]] (+0.67, fdr 1e-05), [[CCDC43]] (+0.67, fdr 7e-06), [[CEBPZ]] (+0.66, fdr 7e-06); moves opposite to [[MXRA7]] (-0.62, fdr 1e-05), [[PRKACA]] (-0.61, fdr 1e-05), [[TXNDC5]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10548.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.43×** | +31.5 | 0e+00 | 48/48 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.30×** | +20.8 | 0e+00 | 48/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.28×** | +20.6 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.17×** | +18.6 | 0e+00 | 46/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +16.1 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.88×** | +13.8 | 1e-41 | 46/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +11.6 | 5e-29 | 44/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.38×** | +11.3 | 7e-28 | 43/48 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +11.1 | 1e-26 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +10.7 | 6e-25 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +9.9 | 1e-21 | 39/48 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +9.6 | 3e-20 | 42/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +8.2 | 1e-14 | 39/48 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.35×** | +7.2 | 2e-11 | 36/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.33×** | +7.1 | 5e-11 | 32/48 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.26×** | +5.7 | 4e-07 | 29/49 (C-33 A, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +5.3 | 4e-06 | 27/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10548.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A549 0.201×, NCI-H1573 0.281×, HEC-1-A 0.285×, NCI-H23 0.338×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (SK-MEL-2 0.333×, HEC-1-A 0.346×, KATO III 0.440×, NCI-H2347 0.467×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.402×, LOX-IMVI 0.356×, H4 0.352×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.584×** | -12.5 | 2e-33 | 39/45 (SK-MEL-2, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.596×** | -12.5 | 2e-33 | 38/44 (A549, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.674×** | -9.9 | 7e-21 | 38/49 (RKO, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.882× | -4.5 | 0.001 | 18/49 (RKO, SW48, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.868× | -3.6 | 0.040 | 13/48 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.875× | -3.4 | 0.069 | 16/47 (hTERT-HPNE, SNU-423, …) | two highest doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.915× | -3.1 | 0.18 | 3/48 (RKO, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10548. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 178 | 13 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +24.4) | [[Dinaciclib (drug)]] 0.5 µM 0.531× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 115 | 13 (4 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +20.9) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -12.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 196 | 11 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +22.0) | [[Dinaciclib (drug)]] 0.05 µM 0.546× (z -11.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 135 | 11 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +20.7) | — |
| [[NCI-H1573 (line)]] | alt | 211 | 9 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +27.4) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -17.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 236 | 10 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.338× (z -15.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 218 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -12.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 135 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +25.4) | [[Dinaciclib (drug)]] 0.05 µM 0.502× (z -8.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 173 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +21.1) | [[Dinaciclib (drug)]] 0.05 µM 0.440× (z -13.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 205 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +17.3) | [[Dinaciclib (drug)]] 0.05 µM 0.513× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 397 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.529× (z -10.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 189 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -16.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 214 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +19.4) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -12.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 132 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +20.6) | — |
| [[A549 (line)]] | wt | 142 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +24.3) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -22.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 132 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +19.7) | — |
| [[CFPAC-1 (line)]] | alt | 165 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +23.6) | [[Dinaciclib (drug)]] 5 µM 0.452× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 149 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.60× (z +17.2) | — |
| [[NCI-H2347 (line)]] | alt | 246 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +21.4) | [[Dinaciclib (drug)]] 0.05 µM 0.467× (z -13.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 270 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +22.3) | [[Dinaciclib (drug)]] 0.05 µM 0.528× (z -9.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 201 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -13.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 169 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +15.5) | [[Dinaciclib (drug)]] 0.05 µM 0.349× (z -10.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 119 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +21.6) | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -11.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 173 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +14.3) | — |
| [[RPMI-7951 (line)]] | alt | 209 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -10.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 271 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +16.4) | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -15.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 126 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +19.3) | — |
| [[SW 900 (line)]] | alt | 129 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +16.9) | — |
| [[SW1417 (line)]] | alt | 177 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +27.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.582× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 139 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +19.9) | [[Dinaciclib (drug)]] 5 µM 0.514× (z -11.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 152 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.2) | — |
| [[COLO 205 (line)]] | alt | 146 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +17.7) | — |
| [[HepG2_C3A (line)]] | wt | 116 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 106 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +18.5) | — |
| [[SHP-77 (line)]] | alt | 179 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -11.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 168 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +21.9) | — |
| [[hTERT-HPNE (line)]] | wt | 157 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -11.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 257 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.431× (z -12.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 174 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 103 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.6) | — |
| [[NCI-H2030 (line)]] | alt | 135 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +18.7) | — |
| [[SNU-1 (line)]] | wt | 171 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -13.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 242 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -12.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 206 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -10.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.8) | — |
| [[NCI-H2122 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 214 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10548), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL46]] | +0.67 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CCDC43]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[IWS1]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[NEMF]] | +0.65 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[ESF1]] | +0.65 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[C1orf131]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[PIGBOS1]] | +0.64 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ZC3H13]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[CWC22]] | +0.64 | +0.58 / +0.62 | both halves | 8e-06 | STRING 430 |
| [[COIL]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ZC3H15]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXRA7]] | -0.62 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[PRKACA]] | -0.61 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.57 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[AKT1]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[EIF4EBP2]] | -0.55 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[RPN1]] | -0.54 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[ILF2]] | -0.53 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[ANKRD30BL]] | -0.53 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[DAP]] | -0.52 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[DHFR]] | -0.52 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[LY6G5B]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[HIPK1]] | -0.52 | -0.35 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.9, 1.1); signed map (-0.6, -18.0). **Vector** length 93.8, 31.8% of its response variance represented; |z| ≥ 3 in 1,348 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.7 | +6.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +8.2 | +7.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.4 | +1.0 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +4.3 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +5.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.8 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.8 | +10.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.8 | -0.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | -3.3 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.1 | -12.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.6 | -0.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -2.5 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | +1.1 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | DEAH-box helicase 36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.2 — chr3:154,272,546-154,324,487 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MLEL1, KIAA1488, RHAU; previously DDX36 |
| Gene groups (HGNC) | DEAH-box helicases; DexD/H helicases |
| Reactome | 3 pathways, smallest: DEx/H-box helicases activate type I IFN and inflammatory cytokines production; Cytosolic sensors of pathogen-associated DNA; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2U1](https://www.uniprot.org/uniprotkb/Q9H2U1) (ATP-dependent DNA/RNA helicase DHX36):

> Multifunctional ATP-dependent helicase that unwinds G-quadruplex (G4) structures. Plays a role in many biological processes such as genomic integrity, gene expression regulations and as a sensor to initiate antiviral responses. G4 structures correspond to helical structures containing guanine tetrads (By similarity). Binds with high affinity to and unwinds G4 structures that are formed in nucleic acids (G4-DNA and G4-RNA). Plays a role in genomic integrity. Converts the G4-RNA structure present …

**Summary**, from NCBI Gene [170506](https://www.ncbi.nlm.nih.gov/gene/170506):

> This gene is a member of the DEAH-box family of RNA-dependent NTPases which are named after the conserved amino acid sequence Asp-Glu-Ala-His in motif II. The protein encoded by this gene has been shown to enhance the deadenylation and decay of mRNAs with 3'-UTR AU-rich elements (ARE-mRNA). The protein has also been shown to resolve into single strands the highly stable tetramolecular DNA configuration (G4) that can form spontaneously in guanine-rich regions of DNA. Alternative splicing results …

**Accessions** — [HGNC:14410](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14410) · Entrez [170506](https://www.ncbi.nlm.nih.gov/gene/170506) · UniProt [Q9H2U1](https://www.uniprot.org/uniprotkb/Q9H2U1) · Ensembl [ENSG00000174953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174953)

## Data

Gene col 10548: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10548); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10548, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10548]; `tensor/DDL_lfc|DDL_z.npy` [10548]; `embed/gene_vectors.npy` [10548]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10548 or target_col == 10548). Every well: [[DHX36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
