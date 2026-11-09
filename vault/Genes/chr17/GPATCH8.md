---
symbol: "GPATCH8"
type: "gene"
col: 11829
ensembl_id: "ENSG00000186566"
name: "G-patch domain containing 8"
location: "17q21.31"
module: 51
arm: "+"
pooled_cpm: 216.37
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# GPATCH8

*G-patch domain containing 8* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 4.04× (z +23.7, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.573× (z -18.1, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (HCT15 0.158×, KATO III 0.311×, NCI-H460 0.340×, A498 0.417×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 0.395×, KATO III 0.452×, A498 0.439×, NCI-H460 0.507×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.500×, A-427 0.603×, HOP62 0.633×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF75A]] (+0.75, fdr 7e-06), [[EID2]] (+0.73, fdr 7e-06), [[MRM2]] (+0.70, fdr 7e-06); moves opposite to [[CRYBB2P1]] (-0.65, fdr 7e-06), [[VAMP1]] (-0.63, fdr 1e-05), [[TFRC]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11829.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.04×** | +23.7 | 0e+00 | 48/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.18×** | +19.7 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +19.5 | 0e+00 | 45/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +14.9 | 0e+00 | 45/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +9.3 | 2e-18 | 37/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +7.5 | 4e-12 | 29/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +7.5 | 6e-12 | 31/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +6.2 | 5e-08 | 24/47 (SW48, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +6.0 | 1e-07 | 0/50 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +5.3 | 8e-06 | 21/48 (SW480, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.7 | 2e-04 | 18/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.4 | 6e-04 | 21/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.6 | 0.012 | 13/48 (HT-29, A498, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.037 | 17/49 (KATO III, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.077 | 11/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11829.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (HCT15 0.158×, KATO III 0.311×, NCI-H460 0.340×, A498 0.417×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 0.395×, KATO III 0.452×, A498 0.439×, NCI-H460 0.507×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.500×, A-427 0.603×, HOP62 0.633×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.573×** | -18.1 | 0e+00 | 46/49 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.578×** | -17.2 | 0e+00 | 41/44 (HCT15, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.661×** | -12.5 | 2e-33 | 35/45 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.831×** | -6.0 | 2e-07 | 26/48 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.841× | -5.6 | 2e-06 | 22/48 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.896× | -5.1 | 4e-05 | 17/49 (A-172, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.898× | -5.0 | 6e-05 | 5/48 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.866× | -4.5 | 4e-04 | 23/50 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.869× | -4.4 | 7e-04 | 22/48 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.904× | -3.0 | 0.12 | 8/47 (PANC-1, SW48, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.911× | -3.0 | 0.12 | 11/49 (SK-MEL-2, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11829. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 265 | 3 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.22× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.633× (z -9.0) |
| [[KATO III (line)]] | alt | 302 | 5 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.86× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -24.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 217 | 4 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.08× (z +14.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -13.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 210 | 5 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.465× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.500× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 187 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.503× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 227 | 6 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.16× (z +19.9) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -24.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 134 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +22.7) | [[Dinaciclib (drug)]] 5 µM 0.440× (z -17.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 196 | 2 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -13.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A498 (line)]] | wt | 192 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -17.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 260 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -16.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 331 | 4 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.24× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.458× (z -15.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 187 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -14.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 172 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +19.1) | [[Dinaciclib (drug)]] 0.5 µM 0.611× (z -9.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 175 | 5 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.38× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 301 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +14.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -14.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 263 | 5 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.35× (z +27.2) | [[Dinaciclib (drug)]] 5 µM 0.578× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 198 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.27× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -15.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 245 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.67× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -13.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 237 | 2 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.47× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.603× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 230 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.15× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.480× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 190 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.88× (z +17.9) | — |
| [[RPMI-7951 (line)]] | alt | 177 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 4.01× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 255 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.594× (z -8.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 212 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.76× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -12.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 151 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 5.19× (z +12.4) | — |
| [[C-33 A (line)]] | alt | 252 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.25× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.430× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 168 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.75× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -17.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 258 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.68× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -13.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 230 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.23× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.538× (z -10.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 186 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.85× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.363× (z -15.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 239 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.04× (z +13.6) | [[Docetaxel (drug)]] 0.05 µM 0.652× (z -8.6) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 142 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +12.7) | — |
| [[COLO 205 (line)]] | alt | 274 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.6× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -12.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 269 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.72× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.158× (z -27.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 268 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.47× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.441× (z -12.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 227 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -14.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 217 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 2.78× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.508× (z -12.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 162 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.01× (z +19.3) | — |
| [[Panc 03.27 (line)]] | alt | 265 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.10× (z +14.6) | — |
| [[SHP-77 (line)]] | alt | 239 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.74× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.587× (z -10.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 197 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.68× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.548× (z -8.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 163 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 117 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +12.6) | — |
| [[AN3 CA (line)]] | alt | 241 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -11.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 409 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 260 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 199 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11829), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF75A]] | +0.75 | +0.72 / +0.66 | both halves | 7e-06 | same gene group |
| [[EID2]] | +0.73 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[MRM2]] | +0.70 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[MAU2]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 | STRING 402 |
| [[ANKRD49]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[BPTF]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[YTHDF2]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[LLPH]] | +0.66 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[IP6K1]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[SCAF8]] | +0.65 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[ZNF3]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYBB2P1]] | -0.65 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[VAMP1]] | -0.63 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[TFRC]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TMED2]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[CSRP2]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[DESI2]] | -0.57 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[EOLA2]] | -0.56 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[SEC61A1]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[MTHFD2]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[HYOU1]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.689). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-41.6, 4.3); signed map (-3.1, -15.9). **Vector** length 121, 38.3% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +11.0 | +23.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.8 | +14.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.1 | +19.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +19.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +7.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +4.3 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.8 | +6.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +3.8 | +2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +3.5 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.3 | -12.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -3.0 | -0.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | G-patch domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,395,281-44,503,430 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0553, GPATC8 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; G-patch domain containing; ZNF804 family |
| Matched by | ensembl_id |

UniProt [Q9UKJ3](https://www.uniprot.org/uniprotkb/Q9UKJ3) carries no function annotation.

**Summary**, from NCBI Gene [23131](https://www.ncbi.nlm.nih.gov/gene/23131):

> The protein encoded by this gene contains an RNA-processing domain, a zinc finger domain, a lysine-rich region and a serine-rich region. A mutation in the serine-rich region of the protein is thought to be associated with hyperuricemia (PMID: 21594610). Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Feb 2015]

**Accessions** — [HGNC:29066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29066) · Entrez [23131](https://www.ncbi.nlm.nih.gov/gene/23131) · UniProt [Q9UKJ3](https://www.uniprot.org/uniprotkb/Q9UKJ3) · Ensembl [ENSG00000186566](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186566)

## Data

Gene col 11829: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11829); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11829, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11829]; `tensor/DDL_lfc|DDL_z.npy` [11829]; `embed/gene_vectors.npy` [11829]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11829 or target_col == 11829). Every well: [[GPATCH8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPATCH8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
