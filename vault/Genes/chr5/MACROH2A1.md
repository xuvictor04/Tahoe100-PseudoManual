---
symbol: "MACROH2A1"
type: "gene"
col: 3488
ensembl_id: "ENSG00000113648"
name: "macroH2A.1 histone"
location: "5q31.1"
module: 4
arm: "+"
pooled_cpm: 130.55
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MACROH2A1

*macroH2A.1 histone* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.10× (z +30.7, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.30× (z +7.2, q 7e-11, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.864× (z -5.6, q 1e-05, down in 22 of 48 measured lines) ⚠ cell-cycle shift, explains ~71% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 0.720× (z -4.7, q 5e-04, down in 22 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-427 0.547×, AN3 CA 0.377×, SK-MEL-2 0.540×, NCI-H460 0.648×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.411×; ⚠ cell-cycle shift, explains ~74% of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (AN3 CA 0.0769×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFDP1]] (+0.72, fdr 7e-06), [[PRKDC]] (+0.72, fdr 7e-06), [[NUDT5]] (+0.72, fdr 7e-06); moves opposite to [[SAT2]] (-0.74, fdr 7e-06), [[NFKBIL1]] (-0.70, fdr 7e-06), [[TERF2IP]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLIN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3488.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.10×** | +30.7 | 0e+00 | 49/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +28.0 | 0e+00 | 44/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.39×** | +21.8 | 0e+00 | 45/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.33×** | +7.5 | 9e-12 | 32/47 (NCI-H1792, COLO 205, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +7.2 | 7e-11 | 31/48 (Panc 03.27, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +6.9 | 5e-10 | 35/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +6.3 | 3e-08 | 25/38 (NCI-H2347, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.26×** | +6.0 | 1e-07 | 26/50 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +5.7 | 7e-07 | 28/48 (HT-29, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.21×** | +5.2 | 1e-05 | 26/48 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.20×** | +5.0 | 3e-05 | 23/48 (HT-29, H4, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.20×** | +4.7 | 2e-04 | 23/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +4.5 | 3e-04 | 20/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 1.18× | +4.3 | 8e-04 | 20/48 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.16× | +4.0 | 0.003 | 20/48 (COLO 205, AsPC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.004 | 20/48 (NCI-H460, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.14× | +3.6 | 0.009 | 16/47 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.010 | 17/48 (NCI-H460, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.14× | +3.4 | 0.016 | 17/47 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Malotilate (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.036 | 9/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.043 | 18/48 (NCI-H460, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Sonidegib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.044 | 13/48 (NCI-H460, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.22×** | +2.8 | 0.091 | 9/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3488.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-427 0.547×, AN3 CA 0.377×, SK-MEL-2 0.540×, NCI-H460 0.648×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.411×; ⚠ cell-cycle shift, explains ~74% of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (AN3 CA 0.0769×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.864× | -5.6 | 1e-05 | 22/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 0.834× | -5.0 | 2e-04 | 23/48 (A498, H4, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.720×** | -4.7 | 5e-04 | 22/49 (A498, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.900× | -4.1 | 0.006 | 11/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.862× | -3.7 | 0.022 | 18/50 (HEC-1-A, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.910× | -3.7 | 0.023 | 4/48 (SNU-1, CHP-212, …) | top dose only | position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | **0.788×** | -3.4 | 0.055 | 15/49 (A-172, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.870× | -3.4 | 0.055 | 10/49 (AsPC-1, A498, …) | all doses, stronger at high dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | 0.856× | -3.0 | 0.13 | 9/48 (Hs 766T, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.925× | -3.0 | 0.13 | 17/48 (A-427, AN3 CA, …) | top dose only | composition shift |
| [[Temsirolimus (drug)]] 5 µM |  | 0.925× | -3.0 | 0.13 | 2/49 (HOP62, NCI-H1792) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3488. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 140 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +19.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.411× (z -12.9) ⚠ cell-cycle shift, explains ~74% of this change |
| [[MIA PaCa-2 (line)]] | alt | 117 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +17.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 121 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.06× (z +24.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.648× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 108 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +16.9) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.650× (z -9.5) ⚠ cell-cycle shift, explains ~71% of this change |
| [[KATO III (line)]] | alt | 118 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +17.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 225 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +23.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.640× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 138 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +16.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 54.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.97× (z +18.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 105 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +16.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.618× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 101 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 159 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +15.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 80.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +15.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 145 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +26.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 149 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +16.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 94.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +18.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 184 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.97× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 90.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +19.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 101 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +13.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 114 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +13.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 238 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 121 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +19.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 87.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +14.1) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 115 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +15.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 184 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +20.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 103 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +17.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 180 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +19.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 98.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +21.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 88.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +16.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 136 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 113 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +9.7) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.397× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 76.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +15.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 98.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +12.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 163 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +13.8) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.26× (z +8.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 171 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +14.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 173 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +14.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 136 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +16.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 111 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +10.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 173 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 132 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +12.0) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 90.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 126 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +8.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 138 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.01× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 178 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +10.9) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3488), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFDP1]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.72 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[NUDT5]] | +0.72 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[GMPS]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[IPO5]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[MAPK9]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[PSME3]] | +0.69 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[PSMD1]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[UGGT1]] | +0.68 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[XRCC5]] | +0.67 | +0.62 / +0.70 | both halves | 7e-06 | STRING 514 |
| [[WDR77]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[NUP205]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAT2]] | -0.74 | -0.69 / -0.73 | both halves | 7e-06 |  |
| [[NFKBIL1]] | -0.70 | -0.62 / -0.72 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.69 | -0.64 / -0.69 | both halves | 7e-06 |  |
| [[SYF2]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.67 | -0.58 / -0.72 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RRAGC]] | -0.67 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[ZFYVE1]] | -0.66 | -0.69 / -0.58 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | -0.66 | -0.57 / -0.69 | both halves | 1e-05 |  |
| [[KRT10]] ⚠ | -0.66 | -0.59 / -0.70 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MED19]] | -0.65 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[CIR1]] | -0.65 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.65 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[PNRC1]] | -0.64 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[TTC21A]] | -0.64 | -0.67 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLIN2]] | B | PLIN2 activity lowers MACROH2A1's level | lines that do not express PLIN2 (17) vs lines expressing it (33) | 1.28× higher at baseline in the lines without PLIN2 | 0.082 | ⚠ within organs, on part of the lines; also absent: AXL, UBE2Q2P13, SLC2A3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.2, -32.6); signed map (-19.8, -46.9). **Vector** length 109, 31.7% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +30.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +28.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +21.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.5 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +5.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +4.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.2 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -5.8 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -4.9 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.0 | -2.0 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | -3.7 | -3.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.4 | -1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.0 | -2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.6 | -0.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.5 | -0.4 |
|  | [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | -2.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | macroH2A.1 histone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:135,334,381-135,399,914 (-) |
| Ensembl biotype | protein_coding |
| Also known as | macroH2A1.2; previously H2AFY |
| Gene groups (HGNC) | Macro domain containing; H2A histones |
| Matched by | ensembl_id |

**Function**, from UniProt [O75367](https://www.uniprot.org/uniprotkb/O75367) (Core histone macro-H2A.1):

> Variant histone H2A which replaces conventional H2A in a subset of nucleosomes where it represses transcription. Nucleosomes wrap and compact DNA into chromatin, limiting DNA accessibility to the cellular machineries which require DNA as a template. Histones thereby play a central role in transcription regulation, DNA repair, DNA replication and chromosomal stability. DNA accessibility is regulated via a complex set of post-translational modifications of histones, also called histone code, and …

**Summary**, from NCBI Gene [9555](https://www.ncbi.nlm.nih.gov/gene/9555):

> Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Nucleosomes consist of approximately 146 bp of DNA wrapped around a histone octamer composed of pairs of each of the four core histones (H2A, H2B, H3, and H4). The chromatin fiber is further compacted through the interaction of a linker histone, H1, with the DNA between the nucleosomes to form higher order chromatin structures. This gene encodes a replication-independent …

**Accessions** — [HGNC:4740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4740) · Entrez [9555](https://www.ncbi.nlm.nih.gov/gene/9555) · UniProt [O75367](https://www.uniprot.org/uniprotkb/O75367) · Ensembl [ENSG00000113648](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113648)

## Data

Gene col 3488: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3488); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3488, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3488]; `tensor/DDL_lfc|DDL_z.npy` [3488]; `embed/gene_vectors.npy` [3488]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3488 or target_col == 3488). Every well: [[MACROH2A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MACROH2A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
