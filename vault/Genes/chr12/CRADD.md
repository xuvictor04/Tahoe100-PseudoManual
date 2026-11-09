---
symbol: "CRADD"
type: "gene"
col: 9799
ensembl_id: "ENSG00000169372"
name: "CARD and death domain containing adaptor protein"
location: "12q22"
module: 1
arm: "+"
pooled_cpm: 87.36
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 35
n_dd_up_clean: 1
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CRADD

*CARD and death domain containing adaptor protein* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 1.31× (z +4.0, q 0.041, up in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RPMI-7951 2.91×, A-427 2.09×, A-172 2.47×, RKO 1.94×; ⚠ cell-cycle shift, would explain all of this change); [[Tucidinostat (drug)]] 5 µM in 3 lines (hTERT-HPNE 3.98×, LOX-IMVI 2.05×, RPMI-7951 2.01×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SK-MEL-2 4.40×; ⚠ cell-cycle shift, explains ~46% of this change).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.448× (z -16.7, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATXN7L1]] (+0.70, fdr 9e-06), [[EPC1]] (+0.67, fdr 1e-05), [[CWC22]] (+0.65, fdr 1e-05); moves opposite to [[UBTD1]] (-0.60, fdr 1e-05), [[CDR2L]] (-0.60, fdr 2e-05), [[TPST2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9799.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RPMI-7951 2.91×, A-427 2.09×, A-172 2.47×, RKO 1.94×; ⚠ cell-cycle shift, would explain all of this change); [[Tucidinostat (drug)]] 5 µM in 3 lines (hTERT-HPNE 3.98×, LOX-IMVI 2.05×, RPMI-7951 2.01×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SK-MEL-2 4.40×; ⚠ cell-cycle shift, explains ~46% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.041 | 26/47 (A549, SW 900, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.27× | +3.5 | 0.13 | 21/47 (KATO III, SW1417, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.25× | +3.2 | 0.19 | 16/47 (RKO, NCI-H23, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.24× | +3.2 | 0.19 | 22/47 (A-172, SK-MEL-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.24× | +3.0 | 0.23 | 18/46 (SW480, NCI-H23, …) | rises with dose |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.24× | +3.0 | 0.23 | 18/47 (HOP62, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9799.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.448×** | -16.7 | 0e+00 | 46/48 (RPMI-7951, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.334×** | -16.2 | 0e+00 | 41/47 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.379×** | -14.3 | 2e-44 | 41/47 (LS 180, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.437×** | -11.7 | 1e-29 | 38/46 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.432×** | -11.5 | 2e-28 | 36/44 (SW48, LS 180, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.488×** | -10.6 | 3e-24 | 38/47 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.514×** | -9.4 | 3e-19 | 37/47 (LOX-IMVI, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.523×** | -9.2 | 3e-18 | 33/43 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.554×** | -8.7 | 2e-16 | 33/47 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.555×** | -8.7 | 2e-16 | 39/48 (NCI-H23, A-427, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.327×** | -8.6 | 3e-16 | 39/48 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.560×** | -8.5 | 6e-16 | 34/47 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.561×** | -8.5 | 6e-16 | 39/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.578×** | -8.1 | 3e-14 | 42/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.567×** | -8.0 | 3e-14 | 39/49 (A-427, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.626×** | -6.9 | 2e-10 | 36/47 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.649×** | -6.0 | 5e-08 | 37/47 (PANC-1, NCI-H661, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.676×** | -5.8 | 2e-07 | 33/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.484×** | -5.6 | 5e-07 | 39/47 (NCI-H1573, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.582×** | -4.2 | 7e-04 | 27/47 (NCI-H460, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.831×** | -3.8 | 0.003 | 23/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.777×** | -3.7 | 0.004 | 26/46 (H4, NCI-H460, …) | two highest doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.837× | -3.7 | 0.004 | 19/48 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.623×** | -3.7 | 0.005 | 22/47 (HEC-1-A, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.800×** | -3.3 | 0.019 | 22/48 (hTERT-HPNE, NCI-H2122, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9799. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 141 | 0 | 17 (13 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -17.1) |
| [[NCI-H1792 (line)]] | alt | 138 | 0 | 15 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -14.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -14.3) |
| [[PANC-1 (line)]] | alt | 69.0 | 0 | 14 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -24.0) |
| [[SW480 (line)]] | alt | 97.1 | 0 | 12 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -22.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -22.2) |
| [[KATO III (line)]] | alt | 91.9 | 0 | 10 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -21.2) |
| [[LS 180 (line)]] | wt | 170 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0903× (z -25.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -22.7) |
| [[HEC-1-A (line)]] | alt | 97.4 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -15.8) |
| [[HepG2_C3A (line)]] | wt | 157 | 0 | 9 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -15.5) |
| [[NCI-H23 (line)]] | alt | 112 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0827× (z -28.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.440× (z -9.4) |
| [[COLO 205 (line)]] | alt | 91.1 | 0 | 7 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.150× (z -14.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -12.5) |
| [[LoVo (line)]] | wt | 150 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -12.9) |
| [[SW48 (line)]] | wt | 118 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0747× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -10.3) |
| [[A-427 (line)]] | wt | 70.7 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0776× (z -27.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.357× (z -11.1) |
| [[H4 (line)]] | wt | 99.5 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -15.7) |
| [[HOP62 (line)]] | alt | 82.9 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 114 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.370× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 132 | 3 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.01× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -17.6) |
| [[AN3 CA (line)]] | alt | 121 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.134× (z -12.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.196× (z -10.2) |
| [[C32 (line)]] | wt | 159 | 0 | 5 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -18.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -15.0) |
| [[MIA PaCa-2 (line)]] | alt | 54.5 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.175× (z -13.9) |
| [[SK-MEL-2 (line)]] | alt | 147 | 3 (3 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.40× (z +14.6) ⚠ cell-cycle shift, explains ~46% of this change | [[Dinaciclib (drug)]] 5 µM 0.271× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -8.7) |
| [[SW 900 (line)]] | alt | 73.6 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -12.0) |
| [[SW1417 (line)]] | alt | 63.4 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -12.1) |
| [[BT-474 (line)]] | alt | 48.1 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 163 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.98× (z +14.5) | [[Docetaxel (drug)]] 0.05 µM 0.243× (z -10.5) ⚠ transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 121 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.05× (z +11.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -14.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -13.4) |
| [[SHP-77 (line)]] | alt | 87.2 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -13.7) |
| [[SNU-1 (line)]] | wt | 141 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -9.9) |
| [[RKO (line)]] | wt | 97.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.213× (z -13.8) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 109 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -8.9) |
| [[A549 (line)]] | wt | 88.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -10.4) |
| [[C-33 A (line)]] | alt | 78.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.352× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 50.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -12.5) |
| [[SW 1271 (line)]] | alt | 88.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0583× (z -10.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 50.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -9.3) |
| [[CHP-212 (line)]] | wt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[HCT15 (line)]] | alt | 111 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.287× (z -10.0) |
| [[Hs 766T (line)]] | wt | 35.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -8.8) |
| [[HS-578T (line)]] | alt | 66.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.205× (z -10.2) ⚠ toxic |
| [[HT-29 (line)]] | alt | 26.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 75.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.358× (z -9.2) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 38.0 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.316× (z -9.0) |
| [[SNU-423 (line)]] | alt | 48.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -8.6) |
| [[A498 (line)]] | wt | 6.19 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9799), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN7L1]] | +0.70 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[EPC1]] | +0.67 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[CWC22]] | +0.65 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[SLX4IP]] | +0.63 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[NFYC]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MRPS33]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[THADA]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[JPX]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[WARS2]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[MRPL15]] | +0.60 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[YTHDC2]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[NOL8]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBTD1]] | -0.60 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[CDR2L]] | -0.60 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[TPST2]] | -0.60 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[P3H1]] | -0.59 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[PDZD7]] | -0.59 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[MXRA7]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[CACNB3]] | -0.57 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[MFN1]] | -0.56 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[RAB43]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[SDHAP4]] | -0.56 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[MBOAT7]] | -0.56 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[NLGN2]] | -0.56 | -0.42 / -0.57 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.9, 11.2); signed map (6.9, -19.2). **Vector** length 83.4, 23.9% of its response variance represented; |z| ≥ 3 in 1,453 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +9.4 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +9.1 | -1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.9 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +0.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +3.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.0 | -0.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -16.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.9 | -9.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.5 | -5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | +1.7 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.6 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | CARD and death domain containing adaptor protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:93,677,375-93,894,840 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAIDD |
| Gene groups (HGNC) | Caspase recruitment domain containing; Caspase-2 PIDDosome complex |
| Reactome | 3 pathways, smallest: TP53 Regulates Transcription of Caspase Activators and Caspases; TP53 Regulates Transcription of Cell Death Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [P78560](https://www.uniprot.org/uniprotkb/P78560) (Death domain-containing protein CRADD):

> Adapter protein that associates with PIDD1 and the caspase CASP2 to form the PIDDosome, a complex that activates CASP2 and triggers apoptosis. Also recruits CASP2 to the TNFR-1 signaling complex through its interaction with RIPK1 and TRADD and may play a role in the tumor necrosis factor-mediated signaling pathway.

**Summary**, from NCBI Gene [8738](https://www.ncbi.nlm.nih.gov/gene/8738):

> This gene encodes a protein containing a death domain (DD) motif. This protein recruits caspase 2/ICH1 to the cell death signal transduction complex, which includes tumor necrosis factor receptor 1 (TNFR1A) and RIPK1/RIP kinase, and acts in promoting apoptosis. A mutation in this gene was associated with cognitive disability. A related pseudogene is found on chromosome 3. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:2340](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2340) · Entrez [8738](https://www.ncbi.nlm.nih.gov/gene/8738) · UniProt [P78560](https://www.uniprot.org/uniprotkb/P78560) · Ensembl [ENSG00000169372](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169372)

## Data

Gene col 9799: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9799); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9799, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9799]; `tensor/DDL_lfc|DDL_z.npy` [9799]; `embed/gene_vectors.npy` [9799]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9799 or target_col == 9799). Every well: [[CRADD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRADD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
