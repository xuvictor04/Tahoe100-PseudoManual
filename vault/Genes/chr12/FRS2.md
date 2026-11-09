---
symbol: "FRS2"
type: "gene"
col: 9264
ensembl_id: "ENSG00000166225"
name: "fibroblast growth factor receptor substrate 2"
location: "12q15"
module: 118
arm: "+"
pooled_cpm: 124.66
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# FRS2

*fibroblast growth factor receptor substrate 2* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 8.02× (z +21.0, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.315× (z -25.7, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 0.798× (z -3.7, q 0.023, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PFDN1]] (+0.67, fdr 8e-06), [[DNAJC30]] (+0.65, fdr 1e-05), [[NSUN3]] (+0.65, fdr 1e-05); moves opposite to [[NPHP4]] (-0.54, fdr 1e-04), [[ARHGEF10]] (-0.53, fdr 1e-04), [[ENTPD4]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 118]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9264.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **8.02×** | +21.0 | 0e+00 | 48/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.48×** | +15.1 | 0e+00 | 47/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +14.5 | 1e-45 | 37/48 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +8.8 | 2e-16 | 45/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +7.8 | 8e-13 | 33/48 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +7.3 | 2e-11 | 40/48 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +7.2 | 4e-11 | 41/48 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +6.8 | 6e-10 | 36/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.23×** | +6.7 | 2e-09 | 29/48 (A498, A549, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +6.5 | 4e-09 | 34/48 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +5.3 | 7e-06 | 29/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +4.3 | 7e-04 | 25/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.3 | 7e-04 | 31/45 (RKO, A-172, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.19× | +4.1 | 0.002 | 19/48 (SNU-1, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.9 | 0.004 | 20/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.8 | 0.005 | 13/48 (SW1417, A-427, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.8 | 0.005 | 17/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.011 | 21/49 (LOX-IMVI, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Baicalin (drug)]] 5 µM |  | 1.09× | +2.9 | 0.082 | 0/49 | top dose only |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.13× | +2.9 | 0.097 | 5/48 (J82, A-427, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9264.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.315×** | -25.7 | 0e+00 | 44/44 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.329×** | -25.6 | 0e+00 | 49/49 (C-33 A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.576×** | -10.5 | 2e-23 | 38/45 (A-427, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~19% of this change | **0.747×** | -6.7 | 2e-09 | 36/48 (J82, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.798×** | -3.7 | 0.023 | 20/47 (SHP-77, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.897× | -3.5 | 0.036 | 6/48 (CFPAC-1, A498, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.808×** | -3.5 | 0.036 | 21/48 (KATO III, Hs 766T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.814×** | -3.4 | 0.051 | 24/48 (SW 900, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9264. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 93.8 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +26.8) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -18.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 118 | 4 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.6× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -20.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 101 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -15.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 142 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -17.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 156 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 11.8× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -19.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 116 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 13.0× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -17.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 89.6 | 3 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 11.6× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -13.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 115 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.7× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.164× (z -29.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 123 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -24.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 108 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.2× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -17.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 105 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -11.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 155 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.1× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 137 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.1× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.0547× (z -37.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 117 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.10× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 134 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.95× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -17.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 133 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -16.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 138 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -23.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 126 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.80× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -17.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 190 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.42× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0553× (z -35.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 102 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 13.0× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -11.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 126 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.97× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -18.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 91.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +17.4) | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -9.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 118 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -15.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 96.5 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.16× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 196 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.29× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -30.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 139 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -20.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 231 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.5× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -27.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 124 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.92× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.403× (z -8.7) |
| [[SW 900 (line)]] | alt | 124 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -18.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 98.1 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.67× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -14.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 118 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 131 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.72× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -14.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 77.7 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.82× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -15.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 99.0 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.9× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 206 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.35× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -21.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 95.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.02× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -19.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 102 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -12.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 110 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 5.93× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0343× (z -29.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 120 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.83× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0411× (z -36.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 88.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 17.7× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -13.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 129 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.79× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -13.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 121 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.4× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -19.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -12.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -11.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 114 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.25× (z +9.4) | — |
| [[NCI-H661 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 193 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9264), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFDN1]] | +0.67 | +0.57 / +0.70 | both halves | 8e-06 |  |
| [[DNAJC30]] | +0.65 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[NSUN3]] | +0.65 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ZNF189]] | +0.64 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[PSMC2]] | +0.61 | +0.54 / +0.47 | both halves | 2e-05 | pathway: Intracellular signaling by second messengers |
| [[SMG8]] | +0.60 | +0.49 / +0.34 | both halves | 1e-04 |  |
| [[LANCL2]] | +0.60 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[PRCC]] | +0.59 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[APPBP2]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[CHD6]] | +0.59 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[GPATCH8]] | +0.58 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[TLK2]] | +0.58 | +0.44 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP4]] | -0.54 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[ARHGEF10]] | -0.53 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[ENTPD4]] | -0.51 | -0.35 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.703). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-47.6, 9.6); signed map (13.5, -25.0). **Vector** length 82.0, 23.7% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +8.4 | +6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.4 | +21.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.2 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +15.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.2 | +0.4 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -0.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.0 | +0.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor receptor substrate 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:69,470,349-69,579,793 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SNT-1, FRS2alpha, SNT1, FRS2A |
| Reactome | 62 pathways, smallest: Activated NTRK2 signals through FRS2 and FRS3; Signaling by FGFR4 in disease; Frs2-mediated activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WU20](https://www.uniprot.org/uniprotkb/Q8WU20) (Fibroblast growth factor receptor substrate 2):

> Adapter protein that links activated FGR and NGF receptors to downstream signaling pathways. Plays an important role in the activation of MAP kinases and in the phosphorylation of PIK3R1, the regulatory subunit of phosphatidylinositol 3-kinase, in response to ligand-mediated activation of FGFR1. Modulates signaling via SHC1 by competing for a common binding site on NTRK1.

**Summary**, from NCBI Gene [10818](https://www.ncbi.nlm.nih.gov/gene/10818):

> Enables fibroblast growth factor receptor binding activity and neurotrophin TRKA receptor binding activity. Involved in negative regulation of cardiac muscle cell differentiation. Acts upstream of or within fibroblast growth factor receptor signaling pathway. Located in adherens junction. Biomarker of renal cell carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16971) · Entrez [10818](https://www.ncbi.nlm.nih.gov/gene/10818) · UniProt [Q8WU20](https://www.uniprot.org/uniprotkb/Q8WU20) · Ensembl [ENSG00000166225](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166225)

## Data

Gene col 9264: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9264); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9264, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9264]; `tensor/DDL_lfc|DDL_z.npy` [9264]; `embed/gene_vectors.npy` [9264]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9264 or target_col == 9264). Every well: [[FRS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
