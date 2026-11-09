---
symbol: "CFDP1"
type: "gene"
col: 7736
ensembl_id: "ENSG00000153774"
name: "chromatin remodeling protein CFDP1"
location: "16q23.1"
module: 52
arm: "+"
pooled_cpm: 217.04
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# CFDP1

*chromatin remodeling protein CFDP1* — 16q23.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H460 1.82×, A-172 1.71×, NCI-H1573 1.48×; ⚠ cell-cycle shift, explains ~42% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 1.72×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 1.63×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 1.78×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.507× (z -22.0, q 0e+00, down in 45 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.649× (z -20.5, q 0e+00, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA1328]] (+0.61, fdr 4e-05), [[SEC22A]] (+0.61, fdr 3e-05), [[ANKS3]] (+0.61, fdr 8e-05); moves opposite to [[TOR1A]] (-0.65, fdr 3e-05), [[ARSB]] (-0.62, fdr 2e-04), [[EIF4G2]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7736.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H460 1.82×, A-172 1.71×, NCI-H1573 1.48×; ⚠ cell-cycle shift, explains ~42% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 1.72×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 1.63×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 1.78×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | 1.12× | +3.7 | 0.12 | 14/49 (A-427, A549, …) | top dose only |  |
| [[Ciclopirox (drug)]] 5 µM |  | 1.07× | +3.2 | 0.45 | 1/48 (AN3 CA) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 24 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7736.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.507×** | -22.0 | 0e+00 | 45/47 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.649×** | -20.5 | 0e+00 | 45/49 (NCI-H2030, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.617×** | -16.2 | 0e+00 | 44/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.618×** | -15.6 | 0e+00 | 42/50 (NCI-H2030, H4, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -15.3 | 0e+00 | 43/48 (MIA PaCa-2, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.694×** | -11.3 | 8e-28 | 35/45 (NCI-H1792, AsPC-1, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.791×** | -11.1 | 8e-27 | 31/48 (C32, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.726×** | -10.7 | 5e-25 | 35/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.746×** | -9.8 | 6e-21 | 32/48 (BT-474, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.741×** | -9.7 | 2e-20 | 29/44 (NCI-H23, NCI-H1792, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.759×** | -8.9 | 3e-17 | 33/48 (C32, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.829×** | -8.9 | 3e-17 | 23/48 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **0.760×** | -8.9 | 3e-17 | 32/47 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.773×** | -8.6 | 3e-16 | 26/48 (BT-474, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.617×** | -8.5 | 8e-16 | 33/38 (SK-MEL-2, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.811×** | -7.0 | 7e-11 | 25/48 (MIA PaCa-2, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.877× | -4.4 | 3e-04 | 14/48 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.782×** | -4.3 | 4e-04 | 18/47 (SW48, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.897× | -3.6 | 0.006 | 8/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.932× | -3.3 | 0.015 | 2/48 (NCI-H2030, HCT15) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.907× | -3.2 | 0.027 | 7/48 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.907× | -3.1 | 0.028 | 0/48 | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.915× | -3.0 | 0.046 | 5/48 (C32, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7736. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 153 | 2 (1 ⚠) | 11 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +16.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.78× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -19.4) |
| [[C32 (line)]] | wt | 196 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -23.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -20.2) |
| [[HOP62 (line)]] | alt | 282 | 0 | 11 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.357× (z -19.0) |
| [[MIA PaCa-2 (line)]] | alt | 370 | 0 | 10 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.355× (z -21.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.383× (z -20.4) |
| [[hTERT-HPNE (line)]] | wt | 219 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -20.2) |
| [[SW480 (line)]] | alt | 300 | 3 (3 ⚠) | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.72× (z +12.9) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.415× (z -20.8) |
| [[HS-578T (line)]] | alt | 214 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 362 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.649× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 497 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -26.0) |
| [[SW 900 (line)]] | alt | 167 | 0 | 8 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.354× (z -14.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.472× (z -10.9) |
| [[A498 (line)]] | wt | 208 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.473× (z -12.6) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 239 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.374× (z -17.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -13.7) |
| [[H4 (line)]] | wt | 273 | 0 | 7 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -15.5) |
| [[A-172 (line)]] | wt | 220 | 1 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.7) ⚠ cell-cycle shift, explains ~42% of this change | [[Auranofin (drug)]] 5 µM 0.289× (z -19.2) |
| [[BT-474 (line)]] | alt | 151 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.339× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 209 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -14.1) |
| [[LS 180 (line)]] | wt | 184 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 223 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.500× (z -13.1) |
| [[SNU-423 (line)]] | alt | 211 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 221 | 0 | 5 (5 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.212× (z -14.7) ⚠ toxic |
| [[SW48 (line)]] | wt | 161 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 228 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -18.1) |
| [[RKO (line)]] | wt | 176 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.385× (z -15.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 153 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.469× (z -11.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 252 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 238 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.405× (z -13.3) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 192 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.373× (z -16.2) |
| [[SW1417 (line)]] | alt | 138 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.500× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 196 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.527× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -10.8) |
| [[A549 (line)]] | wt | 227 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -18.8) |
| [[CHP-212 (line)]] | wt | 285 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -9.4) |
| [[HCT15 (line)]] | alt | 222 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.444× (z -9.9) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 254 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.510× (z -10.6) ⚠ toxic |
| [[HT-29 (line)]] | alt | 172 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.510× (z -11.1) |
| [[J82 (line)]] | alt | 206 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.553× (z -15.1) |
| [[KATO III (line)]] | alt | 198 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.553× (z -9.4) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 191 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.587× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 173 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.313× (z -9.4) ⚠ cell-cycle shift, explains ~17% of this change |
| [[NCI-H2347 (line)]] | alt | 84.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.384× (z -11.3) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.438× (z -12.3) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 138 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -9.4) |
| [[SW 1088 (line)]] | alt | 345 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.135× (z -11.8) |
| [[SW 1271 (line)]] | alt | 207 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.133× (z -9.3) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 191 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 155 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 198 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7736), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1328]] | +0.61 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[SEC22A]] | +0.61 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[ANKS3]] | +0.61 | +0.68 / +0.37 | both halves | 8e-05 |  |
| [[METTL26]] | +0.59 | +0.52 / +0.35 | both halves | 1e-04 |  |
| [[LCMT1]] | +0.59 | +0.61 / +0.32 | both halves | 1e-04 |  |
| [[FRA10AC1]] | +0.59 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[BCAT2]] | +0.58 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[HEATR5B]] | +0.57 | +0.59 / +0.27 | both halves | 3e-04 |  |
| [[ZCCHC7]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[TAMM41]] | +0.57 | +0.56 / +0.30 | both halves | 2e-04 |  |
| [[RARS1]] | +0.57 | +0.60 / +0.37 | both halves | 9e-05 |  |
| [[RAD17]] | +0.57 | +0.53 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOR1A]] | -0.65 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[ARSB]] | -0.62 | -0.62 / -0.32 | both halves | 2e-04 |  |
| [[EIF4G2]] | -0.56 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[MOB1A]] | -0.56 | -0.58 / -0.37 | both halves | 9e-05 |  |
| [[HTR1D]] | -0.53 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[MDFIC]] | -0.53 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[EPM2A]] | -0.53 | -0.42 / -0.21 | both halves | 7e-04 |  |
| [[ARSD]] | -0.53 | -0.40 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[TMEM117]] | -0.52 | -0.55 / -0.25 | both halves | 4e-04 |  |
| [[PPP2CA]] | -0.52 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[MTA2]] | -0.52 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[APPAT]] | -0.52 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[SEPTIN8]] | -0.52 | -0.45 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CFDP1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.305). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (5.6, -14.9); signed map (-40.5, 8.0). **Vector** length 121, 39.0% of its response variance represented; |z| ≥ 3 in 1,306 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.0 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.2 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.7 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.8 | +1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.8 | +2.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.5 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.9 | -11.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.7 | -22.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -15.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.6 | -16.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.6 | -10.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -8.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.0 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.9 | -1.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.9 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | chromatin remodeling protein CFDP1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:75,293,698-75,433,503 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCNT, p97, CP27, SWC5, Yeti, CENP-29 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UEE9](https://www.uniprot.org/uniprotkb/Q9UEE9) (Heterochromatin-stabilizing protein CFDP1):

> Required for the structural stability of pericentromeric heterochromatin. Regulates heterochromatin state by stabilizing CBX5/HP1alpha and H3K9me3 at major satellites and CENPA at minor satellites and is required for incorporation of histone H2AZ1/H2AZ into chromatin (By similarity). Maintenance of chromatin structure promotes binding of guanine-nucleotide releasing factor RCC1 to minor and major satellite repeats (By similarity). Chromatin-bound RCC1 maintains high levels of GTP-bound RAN near …

**Summary**, from NCBI Gene [10428](https://www.ncbi.nlm.nih.gov/gene/10428):

> Predicted to be involved in chromatin remodeling. Predicted to act upstream of or within several processes, including cell adhesion; negative regulation of fibroblast apoptotic process; and regulation of cell shape. Predicted to be located in kinetochore and nucleus. Predicted to be part of Swr1 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1873) · Entrez [10428](https://www.ncbi.nlm.nih.gov/gene/10428) · UniProt [Q9UEE9](https://www.uniprot.org/uniprotkb/Q9UEE9) · Ensembl [ENSG00000153774](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153774)

## Data

Gene col 7736: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7736); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7736, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7736]; `tensor/DDL_lfc|DDL_z.npy` [7736]; `embed/gene_vectors.npy` [7736]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7736 or target_col == 7736). Every well: [[CFDP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFDP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
