---
symbol: "MAD1L1"
type: "gene"
col: 24
ensembl_id: "ENSG00000002822"
name: "mitotic arrest deficient 1 like 1"
location: "7p22.3"
module: 5
arm: "+"
pooled_cpm: 98.65
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MAD1L1

*mitotic arrest deficient 1 like 1* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.32× (z +20.6, q 0e+00, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.524× (z -10.8, q 2e-24, down in 37 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (LoVo 0.270×, SW480 0.312×, NCI-H1573 0.224×, MIA PaCa-2 0.279×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-172 0.222×, NCI-H23 0.290×, SK-MEL-2 0.229×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C32 0.137×, SK-MEL-2 0.225×, HS-578T 0.314×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.522×, C32 0.458×, A-427 0.582×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VAV2]] (+0.71, fdr 7e-06), [[CAPN15]] (+0.61, fdr 1e-05), [[PDCD6]] (+0.61, fdr 1e-05); moves opposite to [[NDUFA5]] (-0.69, fdr 1e-05), [[TAB2]] (-0.65, fdr 1e-05), [[XPA]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 24.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +20.6 | 0e+00 | 42/49 (LS 180, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.53×** | +16.1 | 0e+00 | 46/48 (HCT15, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.05×** | +12.4 | 5e-33 | 45/48 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.81×** | +10.3 | 1e-22 | 42/48 (NCI-H1792, HCT15, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +8.9 | 7e-17 | 26/48 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.63×** | +8.2 | 3e-14 | 34/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.72×** | +7.8 | 6e-13 | 45/48 (NCI-H460, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +6.3 | 2e-08 | 33/48 (SW480, SW48, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.32×** | +4.7 | 2e-04 | 26/50 (LS 180, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +4.5 | 3e-04 | 23/48 (SNU-423, BT-474, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +4.5 | 4e-04 | 26/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.29×** | +4.3 | 7e-04 | 27/48 (COLO 205, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.3 | 7e-04 | 26/45 (NCI-H460, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.007 | 27/48 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.24×** | +3.7 | 0.008 | 24/48 (SW480, COLO 205, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.008 | 25/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.032 | 18/48 (SW480, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.086 | 16/47 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 24.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (LoVo 0.270×, SW480 0.312×, NCI-H1573 0.224×, MIA PaCa-2 0.279×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-172 0.222×, NCI-H23 0.290×, SK-MEL-2 0.229×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C32 0.137×, SK-MEL-2 0.225×, HS-578T 0.314×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.522×, C32 0.458×, A-427 0.582×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.524×** | -10.8 | 2e-24 | 37/44 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.642×** | -7.7 | 3e-12 | 35/49 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.700×** | -5.8 | 2e-06 | 30/45 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.879× | -3.2 | 0.20 | 18/48 (A498, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.832× | -3.1 | 0.23 | 16/49 (CFPAC-1, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 24. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 116 | 10 (7 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.09× (z +13.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -13.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 91.5 | 3 (2 ⚠) | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +19.4) | [[Harringtonine (drug)]] 0.5 µM 0.398× (z -10.7) ⚠ cell-cycle shift, explains ~15% of this change |
| [[LS 180 (line)]] | wt | 61.4 | 6 (5 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +22.6) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 167 | 1 | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.522× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 71.9 | 5 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +16.5) | [[Harringtonine (drug)]] 0.5 µM 0.448× (z -9.5) ⚠ cell-cycle shift, explains ~15% of this change |
| [[C32 (line)]] | wt | 166 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.458× (z -9.4) |
| [[HS-578T (line)]] | alt | 112 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +22.5) | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -12.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 113 | 4 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 156 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +23.0) | — |
| [[SNU-423 (line)]] | alt | 43.5 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +13.0) | — |
| [[A-172 (line)]] | wt | 120 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -17.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 51.7 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +17.1) | — |
| [[AsPC-1 (line)]] | alt | 114 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.48× (z +12.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 35.2 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +15.2) | — |
| [[COLO 205 (line)]] | alt | 113 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.87× (z +19.9) | — |
| [[HCT15 (line)]] | alt | 85.7 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.81× (z +15.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +14.1) | — |
| [[HEC-1-A (line)]] | alt | 76.6 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +18.1) | — |
| [[HT-29 (line)]] | alt | 85.4 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +20.3) | — |
| [[J82 (line)]] | alt | 82.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +15.4) | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -9.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 108 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -14.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 100 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.335× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.582× (z -8.6) |
| [[HOP62 (line)]] | alt | 85.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -10.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 86.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +13.8) | — |
| [[KATO III (line)]] | alt | 110 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +12.7) | — |
| [[Panc 03.27 (line)]] | alt | 78.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +14.3) | — |
| [[PANC-1 (line)]] | alt | 105 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.422× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 101 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -10.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 162 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +16.5) | — |
| [[SHP-77 (line)]] | alt | 140 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 65.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +14.5) | — |
| [[SW1417 (line)]] | alt | 96.2 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0523× (z -11.8) ⚠ toxic |
| [[BT-474 (line)]] | alt | 112 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +12.4) | — |
| [[hTERT-HPNE (line)]] | wt | 56.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 37.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.47× (z +8.5) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 5 µM 0.224× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 58.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +9.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SNU-1 (line)]] | wt | 68.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +17.2) | — |
| [[SW48 (line)]] | wt | 174 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +12.8) | — |
| [[C-33 A (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -11.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 51.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.323× (z -10.7) ⚠ cell-cycle shift, explains ~88% of this change |
| [[NCI-H23 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -14.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 280 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 24), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAV2]] | +0.71 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[CAPN15]] | +0.61 | +0.49 / +0.66 | both halves | 1e-05 | same gene group |
| [[PDCD6]] | +0.61 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[MYO19]] | +0.60 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[XXYLT1]] | +0.60 | +0.52 / +0.64 | both halves | 1e-05 | same gene group |
| [[NPIPB11]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[PRDM15]] | +0.59 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[TRIM65]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[ARPC5L]] | +0.59 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[AXIN1]] | +0.58 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[TOMM40]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[BUD23]] | +0.58 | +0.45 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA5]] | -0.69 | -0.50 / -0.76 | both halves | 1e-05 |  |
| [[TAB2]] | -0.65 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[XPA]] | -0.64 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[ETFRF1]] | -0.63 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[KPNA5]] | -0.63 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[VAPA]] | -0.59 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[COPS5]] | -0.59 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[PHF3]] | -0.58 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[CHURC1]] | -0.58 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[IFTAP]] | -0.57 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[ABCA5]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[SCRN3]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MAD1L1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[WNK2]] | B | WNK2 activity raises MAD1L1's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.08× lower at baseline in the lines without WNK2 | 0.089 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.547). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-22.5, 2.8); signed map (0.4, -53.2). **Vector** length 110, 33.5% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +20.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.1 | +8.2 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -7.0 | -2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.1 | -0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | mitotic arrest deficient 1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:1,815,793-2,233,243 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HsMAD1, TXBP181, MAD1, PIG9, TP53I9 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6D9](https://www.uniprot.org/uniprotkb/Q9Y6D9) (Mitotic spindle assembly checkpoint protein MAD1):

> Component of the spindle-assembly checkpoint that prevents the onset of anaphase until all chromosomes are properly aligned at the metaphase plate. Forms a heterotetrameric complex with the closed conformation form of MAD2L1 (C-MAD2) at unattached kinetochores during prometaphase, recruits an open conformation of MAD2L1 (O-MAD2) and promotes the conversion of O-MAD2 to C-MAD2, which ensures mitotic checkpoint signaling.; [Isoform 3]: Sequesters MAD2L1 in the cytoplasm preventing its function as …

**Summary**, from NCBI Gene [8379](https://www.ncbi.nlm.nih.gov/gene/8379):

> MAD1L1 is a component of the mitotic spindle-assembly checkpoint that prevents the onset of anaphase until all chromosome are properly aligned at the metaphase plate. MAD1L1 functions as a homodimer and interacts with MAD2L1. MAD1L1 may play a role in cell cycle control and tumor suppression. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:6762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6762) · Entrez [8379](https://www.ncbi.nlm.nih.gov/gene/8379) · UniProt [Q9Y6D9](https://www.uniprot.org/uniprotkb/Q9Y6D9) · Ensembl [ENSG00000002822](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000002822)

## Data

Gene col 24: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 24); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 24, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 24]; `tensor/DDL_lfc|DDL_z.npy` [24]; `embed/gene_vectors.npy` [24]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 24 or target_col == 24). Every well: [[MAD1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAD1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
