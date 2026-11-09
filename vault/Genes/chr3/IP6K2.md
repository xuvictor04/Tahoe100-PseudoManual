---
symbol: "IP6K2"
type: "gene"
col: 899
ensembl_id: "ENSG00000068745"
name: "inositol hexakisphosphate kinase 2"
location: "3p21.31"
module: 118
arm: "+"
pooled_cpm: 69.43
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# IP6K2

*inositol hexakisphosphate kinase 2* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.08× (z +14.9, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.417× (z -21.3, q 0e+00, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.788× (z -6.0, q 3e-07, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (SW 900 0.0506×, NCI-H2347 0.242×, NCI-H1573 0.135×, SW480 0.302×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.254×, NCI-H23 0.318×, A-427 0.337×, C-33 A 0.292×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.390×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.356×); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.553×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH3]] (+0.56, fdr 2e-05), [[NAPA-AS1]] (+0.54, fdr 8e-05), [[ZNF493]] (+0.54, fdr 5e-05); moves opposite to [[UCHL5]] (-0.63, fdr 3e-05), [[DNAJC10]] (-0.62, fdr 2e-05), [[GNPNAT1]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 899.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.08×** | +14.9 | 0e+00 | 47/49 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +13.5 | 4e-39 | 32/48 (A498, COLO 205, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +12.2 | 7e-32 | 42/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +11.3 | 2e-27 | 38/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +10.4 | 2e-23 | 40/48 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +9.7 | 4e-20 | 42/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +8.2 | 1e-14 | 32/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +6.9 | 3e-10 | 31/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +6.3 | 2e-08 | 28/48 (HEC-1-A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +6.0 | 1e-07 | 25/47 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +5.5 | 1e-06 | 25/48 (HEC-1-A, NCI-H2030, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +4.8 | 9e-05 | 22/48 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.21×** | +4.7 | 9e-05 | 19/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.4 | 4e-04 | 23/44 (SW1417, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +4.3 | 6e-04 | 23/49 (LS 180, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.029 | 7/48 (SW480, HT-29, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 899.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (SW 900 0.0506×, NCI-H2347 0.242×, NCI-H1573 0.135×, SW480 0.302×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2347 0.254×, NCI-H23 0.318×, A-427 0.337×, C-33 A 0.292×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.390×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.356×); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.553×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.417×** | -21.3 | 0e+00 | 35/44 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.537×** | -15.8 | 0e+00 | 41/49 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.788×** | -6.0 | 3e-07 | 22/48 (NCI-H2347, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.792×** | -5.9 | 4e-07 | 25/48 (Panc 03.27, LOX-IMVI, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | **0.792×** | -5.5 | 5e-06 | 25/45 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.819×** | -5.1 | 4e-05 | 25/48 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.826×** | -4.9 | 1e-04 | 20/48 (LOX-IMVI, NCI-H23, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.833× | -4.6 | 3e-04 | 22/48 (NCI-H23, C32, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.838× | -4.5 | 4e-04 | 22/48 (NCI-H2347, LOX-IMVI, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | 0.839× | -4.4 | 5e-04 | 16/48 (LS 180, HS-578T, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.952× | -4.4 | 5e-04 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.843× | -4.2 | 0.001 | 18/48 (NCI-H2347, C32, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.850× | -4.1 | 0.002 | 21/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.861× | -3.8 | 0.006 | 8/49 (A549, A498, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.857× | -3.8 | 0.006 | 16/48 (LOX-IMVI, RKO, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.867× | -3.6 | 0.009 | 16/48 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.774×** | -3.4 | 0.020 | 14/49 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.913× | -3.3 | 0.030 | 6/48 (MIA PaCa-2, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 899. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 82.6 | 1 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.85× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -15.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 97.4 | 3 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.29× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -16.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 77.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 116 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.21× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.553× (z -8.8) |
| [[SW480 (line)]] | alt | 98.0 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -19.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 64.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -11.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 70.3 | 2 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.21× (z +8.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -10.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 57.7 | 2 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.57× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 74.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -16.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 66.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.468× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 52.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.85× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.135× (z -20.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 57.6 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.60× (z +9.7) | [[AZD2858 (drug)]] 0.5 µM 0.327× (z -8.5) ⚠ toxic |
| [[SW1417 (line)]] | alt | 121 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -12.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 78.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.91× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -13.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 85.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -18.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 47.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.6) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.356× (z -9.9) |
| [[HT-29 (line)]] | alt | 60.3 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.61× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 78.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.57× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 64.3 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +9.6) | — |
| [[RKO (line)]] | wt | 91.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -12.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 57.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 37.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.4) | — |
| [[AN3 CA (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0856× (z -15.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 58.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +9.1) | — |
| [[C32 (line)]] | wt | 72.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -9.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 43.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 40.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.3) | — |
| [[H4 (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -10.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 91.1 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.263× (z -8.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 59.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 46.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -9.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 47.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.57× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 79.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -11.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 63.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -10.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 64.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0506× (z -29.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 94.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -12.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 98.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 899), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH3]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[NAPA-AS1]] | +0.54 | +0.46 / +0.37 | both halves | 8e-05 |  |
| [[ZNF493]] | +0.54 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[IST1]] | +0.53 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[WDR83OS]] ⚠ | +0.53 | +0.43 / +0.57 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[IGBP1]] | +0.53 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[PI4KB]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[FRS2]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[B9D2]] | +0.52 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[YTHDF3]] | +0.52 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[NDUFA13]] ⚠ | +0.52 | +0.33 / +0.54 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ARMC5]] | +0.52 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[NGDN]] | +0.51 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[TRA2A]] | +0.51 | +0.34 / +0.56 | both halves | 1e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UCHL5]] | -0.63 | -0.43 / -0.73 | both halves | 3e-05 |  |
| [[DNAJC10]] | -0.62 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[GNPNAT1]] | -0.57 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[TTC13]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[FARSB]] | -0.50 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[PRKDC]] | -0.50 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[FAM120A]] | -0.49 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[AIDA]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[IPO5]] | -0.49 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[ZWILCH]] | -0.48 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[IDH3A]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[RSC1A1]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises IP6K2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-27.3, -35.5); signed map (-6.4, -6.6). **Vector** length 98.3, 24.6% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.3 | +6.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +13.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.7 | +4.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +14.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +6.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.7 | +1.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.5 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +4.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.6 | -6.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -21.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.4 | -15.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -4.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.7 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | inositol hexakisphosphate kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,688,003-48,740,353 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously IHPK2 |
| Gene groups (HGNC) | Inositol hexakisphosphate kinase family |
| Hallmark sets | P53_PATHWAY |
| Reactome | 5 pathways, smallest: Synthesis of IPs in the nucleus; Interferon alpha/beta signaling; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHH9](https://www.uniprot.org/uniprotkb/Q9UHH9) (Inositol hexakisphosphate kinase 2):

> Converts inositol hexakisphosphate (InsP6) to diphosphoinositol pentakisphosphate (InsP7/PP-InsP5).

**Summary**, from NCBI Gene [51447](https://www.ncbi.nlm.nih.gov/gene/51447):

> This gene encodes a protein that belongs to the inositol phosphokinase (IPK) family. This protein is likely responsible for the conversion of inositol hexakisphosphate (InsP6) to diphosphoinositol pentakisphosphate (InsP7/PP-InsP5). It may also convert 1,3,4,5,6-pentakisphosphate (InsP5) to PP-InsP4 and affect the growth suppressive and apoptotic activities of interferon-beta in some ovarian cancers. Alternative splicing results in multiple transcript variants encoding different isoforms. …

**Accessions** — [HGNC:17313](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17313) · Entrez [51447](https://www.ncbi.nlm.nih.gov/gene/51447) · UniProt [Q9UHH9](https://www.uniprot.org/uniprotkb/Q9UHH9) · Ensembl [ENSG00000068745](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068745)

## Data

Gene col 899: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 899); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 899, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 899]; `tensor/DDL_lfc|DDL_z.npy` [899]; `embed/gene_vectors.npy` [899]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 899 or target_col == 899). Every well: [[IP6K2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IP6K2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
