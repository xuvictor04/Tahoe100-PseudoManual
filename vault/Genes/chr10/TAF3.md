---
symbol: "TAF3"
type: "gene"
col: 9153
ensembl_id: "ENSG00000165632"
name: "TATA-box binding protein associated factor 3"
location: "10p14"
module: 48
arm: "+"
pooled_cpm: 108.2
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 3
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# TAF3

*TATA-box binding protein associated factor 3* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.68× (z +27.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.577× (z -15.1, q 0e+00, down in 35 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.830× (z -5.1, q 6e-05, down in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H2030 0.209×, SW480 0.364×, NCI-H1573 0.227×, J82 0.377×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.187×, LoVo 0.358×, NCI-H2030 0.373×, SW480 0.521×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (RKO 0.211×, NCI-H2030 0.246×, SK-MEL-2 0.220×, SW1417 0.478×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.0879×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.582×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SELENOH]] (+0.60, fdr 3e-05), [[NDUFA4]] (+0.59, fdr 3e-05), [[GPX1]] (+0.59, fdr 6e-05); moves opposite to [[PRELID3B]] (-0.56, fdr 2e-05), [[CSRP1]] (-0.54, fdr 5e-05), [[ZNF460]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.68×** | +27.0 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.46×** | +24.6 | 0e+00 | 48/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.42×** | +24.1 | 0e+00 | 48/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +23.8 | 0e+00 | 44/49 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +16.3 | 0e+00 | 47/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +16.1 | 0e+00 | 46/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +12.8 | 2e-35 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +12.4 | 1e-33 | 39/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +11.6 | 3e-29 | 40/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +11.1 | 9e-27 | 36/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.51×** | +10.8 | 3e-25 | 39/50 (NCI-H460, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +10.6 | 1e-24 | 37/49 (A498, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +10.5 | 6e-24 | 45/48 (SW1417, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +10.3 | 2e-23 | 29/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +8.9 | 2e-17 | 33/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +8.5 | 9e-16 | 25/48 (SNU-1, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +7.0 | 7e-11 | 42/49 (HT-29, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9153.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H2030 0.209×, SW480 0.364×, NCI-H1573 0.227×, J82 0.377×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.187×, LoVo 0.358×, NCI-H2030 0.373×, SW480 0.521×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (RKO 0.211×, NCI-H2030 0.246×, SK-MEL-2 0.220×, SW1417 0.478×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.0879×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.582×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.577×** | -15.1 | 0e+00 | 35/49 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.576×** | -14.5 | 3e-45 | 34/44 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.830×** | -5.1 | 6e-05 | 23/47 (NCI-H2030, hTERT-HPNE, …) | two highest doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.840× | -4.4 | 0.001 | 22/45 (RKO, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.882× | -3.5 | 0.060 | 11/48 (A498, A549, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.890× | -3.2 | 0.12 | 4/48 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.887× | -3.2 | 0.12 | 16/47 (J82, hTERT-HPNE, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 89.9 | 14 (5 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -12.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 141 | 13 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -20.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 166 | 12 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 94.6 | 10 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.3× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -10.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 114 | 8 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +17.2) | [[Dinaciclib (drug)]] 0.05 µM 0.509× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 140 | 10 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +17.9) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -16.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 102 | 9 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 96.2 | 8 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.465× (z -11.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 102 | 7 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.421× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 123 | 7 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.98× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 141 | 6 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 143 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.49× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -22.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 60.3 | 7 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.41× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.538× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 75.3 | 8 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +12.9) | — |
| [[A549 (line)]] | wt | 151 | 5 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.85× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -12.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 85.4 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +13.9) | — |
| [[J82 (line)]] | alt | 107 | 6 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 139 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.60× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.465× (z -10.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 68.1 | 6 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.03× (z +14.0) | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 147 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.25× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -26.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.582× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 123 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.67× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -10.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 117 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.472× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 47.0 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.60× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -15.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 150 | 4 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.478× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 172 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.03× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -13.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 92.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.58× (z +14.1) | — |
| [[C-33 A (line)]] | alt | 93.4 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +13.7) | — |
| [[COLO 205 (line)]] | alt | 135 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -12.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 72.2 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +12.6) | [[Lonafarnib (drug)]] 5 µM 0.205× (z -8.8) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 85.8 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.45× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 80.5 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.87× (z +13.3) | — |
| [[SW 900 (line)]] | alt | 98.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.69× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 55.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.67× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 101 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.69× (z +14.6) | — |
| [[SNU-423 (line)]] | alt | 91.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +10.4) | — |
| [[SW48 (line)]] | wt | 118 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 86.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +14.3) | — |
| [[HCT15 (line)]] | alt | 117 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.82× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 163 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.23× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 107 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.26× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 107 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.30× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.437× (z -9.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 50.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +12.8) | — |
| [[H4 (line)]] | wt | 68.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +11.4) | — |
| [[AN3 CA (line)]] | alt | 83.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +8.5) | — |
| [[NCI-H596 (line)]] | alt | 99.0 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.0879× (z -9.9) |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 11 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOH]] | +0.60 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[NDUFA4]] | +0.59 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[GPX1]] | +0.59 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[COX6B1]] | +0.58 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[MED4]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 | STRING 803 |
| [[PPP4R3A]] | +0.56 | +0.46 / +0.49 | both halves | 3e-05 | same gene group |
| [[MRPL51]] ⚠ | +0.56 | +0.35 / +0.55 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS27L]] | +0.56 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[WDR83OS]] ⚠ | +0.56 | +0.44 / +0.49 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PPM1D]] | +0.56 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[RPS19]] | +0.56 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[UBL5]] | +0.56 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[BMS1P1]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[NDUFA1]] | +0.55 | +0.41 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRELID3B]] | -0.56 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[CSRP1]] | -0.54 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[ZNF460]] | -0.52 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[TEX261]] | -0.52 | -0.26 / -0.43 | both halves | 3e-04 |  |
| [[GTF2A1]] | -0.51 | -0.39 / -0.41 | both halves | 5e-05 | pathway: HIV Infection; STRING 979 |
| [[PSMG1]] | -0.51 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[DBN1]] | -0.51 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[STYX]] | -0.50 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[NUP188]] | -0.50 | -0.35 / -0.46 | both halves | 1e-04 | same gene group; pathway: HIV Infection |
| [[GTF2H3]] | -0.49 | -0.24 / -0.46 | both halves | 4e-04 | pathway: HIV Infection; STRING 979 |
| [[PFKM]] | -0.49 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[NRAS]] | -0.49 | -0.38 / -0.56 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TAF3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.589). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-48.6, -23.0); signed map (-37.2, 9.6). **Vector** length 97.8, 30.0% of its response variance represented; |z| ≥ 3 in 1,554 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Complex I biogenesis* (reactome, mean cos +0.51 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +11.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +16.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.4 | +5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.3 | +6.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.2 | +3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +5.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +3.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.7 | -14.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -9.2 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.1 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.8 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.7 | -15.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:7,818,497-8,016,631 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAF140, TAFII140 |
| Gene groups (HGNC) | PHD finger proteins; Armadillo like helical domain containing; General transcription factor IID complex subunits |
| Reactome | 19 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VWG9](https://www.uniprot.org/uniprotkb/Q5VWG9) (Transcription initiation factor TFIID subunit 3):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription. TFIID recognizes and binds promoters with or without a TATA box via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13. The TFIID complex …

**Summary**, from NCBI Gene [83860](https://www.ncbi.nlm.nih.gov/gene/83860):

> The highly conserved RNA polymerase II transcription factor TFIID (see TAF1; MIM 313650) comprises the TATA box-binding protein (TBP; MIM 600075) and a set of TBP-associated factors (TAFs), including TAF3. TAFs contribute to promoter recognition and selectivity and act as antiapoptotic factors (Gangloff et al., 2001 [PubMed 11438666]).[supplied by OMIM, May 2009]

**Accessions** — [HGNC:17303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17303) · Entrez [83860](https://www.ncbi.nlm.nih.gov/gene/83860) · UniProt [Q5VWG9](https://www.uniprot.org/uniprotkb/Q5VWG9) · Ensembl [ENSG00000165632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165632)

## Data

Gene col 9153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9153); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9153]; `tensor/DDL_lfc|DDL_z.npy` [9153]; `embed/gene_vectors.npy` [9153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9153 or target_col == 9153). Every well: [[TAF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
