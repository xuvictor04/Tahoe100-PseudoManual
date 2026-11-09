---
symbol: "CFL1"
type: "gene"
col: 10290
ensembl_id: "ENSG00000172757"
name: "cofilin 1"
location: "11q13.1"
module: 20
arm: "+"
pooled_cpm: 185.71
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# CFL1

*cofilin 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.52× (z +16.7, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.12× (z +14.3, q 3e-44, up in 48 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (NCI-H1792 6.63×, CFPAC-1 4.71×, A549 4.88×, AsPC-1 3.34×, …); [[Dinaciclib (drug)]] 0.5 µM in 10 lines (SW480 9.14×, HOP62 11.0×, NCI-H460 9.91×, A549 10.7×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 16.3×, C32 5.94×; ⚠ cell-cycle shift, would explain all of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.474×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKM]] (+0.67, fdr 7e-06), [[EIF5A]] (+0.64, fdr 7e-06), [[GPAA1]] (+0.63, fdr 1e-05); moves opposite to [[MRPL21]] (-0.66, fdr 1e-05), [[DYNC2LI1]] (-0.63, fdr 1e-05), [[EPB41L4A-AS1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 16 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10290.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (NCI-H1792 6.63×, CFPAC-1 4.71×, A549 4.88×, AsPC-1 3.34×, …); [[Dinaciclib (drug)]] 0.5 µM in 10 lines (SW480 9.14×, HOP62 11.0×, NCI-H460 9.91×, A549 10.7×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 16.3×, C32 5.94×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **6.52×** | +16.7 | 0e+00 | 49/49 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **5.49×** | +14.6 | 1e-45 | 44/44 (HOP62, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.12×** | +14.3 | 3e-44 | 48/49 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **4.12×** | +11.6 | 4e-29 | 45/45 (HOP62, HS-578T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **2.07×** | +6.4 | 1e-08 | 47/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.09×** | +6.3 | 3e-08 | 48/50 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.8 | 5e-07 | 46/48 (HOP62, A-172, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.55×** | +5.5 | 3e-06 | 28/48 (NCI-H1792, C32, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +5.2 | 1e-05 | 40/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.78×** | +4.9 | 5e-05 | 41/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.72×** | +4.8 | 8e-05 | 40/48 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | **1.71×** | +4.6 | 2e-04 | 34/47 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~78% of this change | **1.62×** | +4.3 | 9e-04 | 43/48 (HCT15, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.47×** | +3.4 | 0.026 | 29/48 (SW480, NCI-H1792, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.4 | 0.027 | 29/38 (NCI-H2347, A-172, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10290.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.474×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.610× | -3.6 | 0.15 | 39/50 (SW480, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.510× | -3.1 | 0.46 | 39/50 (AsPC-1, BT-474, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10290. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 183 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +14.3) | — |
| [[C32 (line)]] | wt | 164 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.94× (z +18.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +15.2) | — |
| [[SNU-423 (line)]] | alt | 163 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +14.1) | — |
| [[LOX-IMVI (line)]] | wt | 189 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.07× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +13.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 118 | 6 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +14.9) | — |
| [[SW480 (line)]] | alt | 157 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.14× (z +17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +13.2) | — |
| [[A-172 (line)]] | wt | 182 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.23× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +13.6) | — |
| [[CFPAC-1 (line)]] | alt | 181 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +15.8) | — |
| [[HS-578T (line)]] | alt | 223 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.66× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +13.1) | — |
| [[hTERT-HPNE (line)]] | wt | 170 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.07× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +12.9) | — |
| [[LoVo (line)]] | wt | 125 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.12× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 189 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.47× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 73.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +23.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.63× (z +16.0) | — |
| [[NCI-H460 (line)]] | wt | 92.3 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.91× (z +16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +15.3) | — |
| [[PANC-1 (line)]] | alt | 266 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.61× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 222 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +10.3) | — |
| [[A498 (line)]] | wt | 159 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.18× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +10.6) | — |
| [[A549 (line)]] | wt | 161 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +15.8) | — |
| [[HEC-1-A (line)]] | alt | 187 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 216 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.52× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 209 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.80× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +11.2) | — |
| [[J82 (line)]] | alt | 335 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +10.1) | — |
| [[KATO III (line)]] | alt | 198 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.23× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 318 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 172 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +14.3) | — |
| [[SNU-1 (line)]] | wt | 128 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.25× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 159 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 216 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +12.6) | — |
| [[SW48 (line)]] | wt | 127 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.30× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +10.4) | — |
| [[A-427 (line)]] | wt | 310 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 148 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.39× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[AsPC-1 (line)]] | alt | 211 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +15.3) | — |
| [[C-33 A (line)]] | alt | 173 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[CHP-212 (line)]] | wt | 126 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.39× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +8.7) | — |
| [[H4 (line)]] | wt | 174 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.96× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +11.6) | — |
| [[HCT15 (line)]] | alt | 131 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.65× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 185 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.00× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2347 (line)]] | alt | 223 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +14.5) | — |
| [[RKO (line)]] | wt | 170 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.27× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +11.0) | — |
| [[SHP-77 (line)]] | alt | 166 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 117 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[BT-474 (line)]] | alt | 242 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 82.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.4× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 199 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW 1271 (line)]] | alt | 139 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 156 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 176 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10290), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*20 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKM]] | +0.67 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[EIF5A]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 | STRING 522 |
| [[GPAA1]] | +0.63 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[PPIA]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 | pathway: Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; STRING 880 |
| [[FLNA]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 916 |
| [[BSG]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[TAGLN2]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 716 |
| [[SNRPB]] | +0.57 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ACTB]] | +0.55 | +0.66 / +0.48 | both halves | 2e-05 | pathway: EPH-Ephrin signaling; STRING 999 |
| [[TMBIM6]] | +0.55 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[CALM2]] | +0.53 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[PFN1]] | +0.53 | +0.61 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING; STRING 994 |

## Genes that move opposite

*80 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL21]] | -0.66 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[DYNC2LI1]] | -0.63 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | -0.63 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[RBMX2]] | -0.63 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[DNAJC2]] | -0.63 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[EFCAB7]] | -0.59 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[NOL7]] ⚠ | -0.59 | -0.60 / -0.47 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RUFY2]] | -0.57 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[DDX19B]] | -0.57 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[METTL5]] | -0.57 | -0.35 / -0.64 | both halves | 1e-04 |  |
| [[BBS5]] | -0.57 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[C19orf44]] | -0.57 | -0.31 / -0.68 | both halves | 2e-04 |  |
| [[LIAS]] | -0.57 | -0.47 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CFL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.298). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.8, -10.3); signed map (-28.4, -41.2). **Vector** length 90.9, 42.5% of its response variance represented; |z| ≥ 3 in 1,057 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +14.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.7 | +6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | +3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.3 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +1.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +2.4 | -0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +0.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.9 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -0.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -4.1 | +16.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.7 | -0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | cofilin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,823,022-65,862,026 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CFL |
| Gene groups (HGNC) | Cofilin family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 22 pathways, smallest: Sema3A PAK dependent Axon repulsion; RHO GTPases Activate ROCKs; Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P23528](https://www.uniprot.org/uniprotkb/P23528) (Cofilin-1):

> Binds to F-actin and exhibits pH-sensitive F-actin depolymerizing activity. In conjunction with the subcortical maternal complex (SCMC), plays an essential role for zygotes to progress beyond the first embryonic cell divisions via regulation of actin dynamics. Required for the centralization of the mitotic spindle and symmetric division of zygotes (By similarity). Plays a role in the regulation of cell morphology and cytoskeletal organization in epithelial cells. Required for the up-regulation …

**Summary**, from NCBI Gene [1072](https://www.ncbi.nlm.nih.gov/gene/1072):

> The protein encoded by this gene can polymerize and depolymerize F-actin and G-actin in a pH-dependent manner. Increased phosphorylation of this protein by LIM kinase aids in Rho-induced reorganization of the actin cytoskeleton. Cofilin is a widely distributed intracellular actin-modulating protein that binds and depolymerizes filamentous F-actin and inhibits the polymerization of monomeric G-actin in a pH-dependent manner. It is involved in the translocation of actin-cofilin complex from …

**Accessions** — [HGNC:1874](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1874) · Entrez [1072](https://www.ncbi.nlm.nih.gov/gene/1072) · UniProt [P23528](https://www.uniprot.org/uniprotkb/P23528) · Ensembl [ENSG00000172757](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172757)

## Data

Gene col 10290: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10290); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10290, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10290]; `tensor/DDL_lfc|DDL_z.npy` [10290]; `embed/gene_vectors.npy` [10290]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10290 or target_col == 10290). Every well: [[CFL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
