---
symbol: "MIDEAS"
type: "gene"
col: 7942
ensembl_id: "ENSG00000156030"
name: "mitotic deacetylase associated SANT domain protein"
location: "14q24.3"
module: 14
arm: "+"
pooled_cpm: 118.57
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 16
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# MIDEAS

*mitotic deacetylase associated SANT domain protein* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.73× (z +25.8, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.299× (z -17.1, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.511× (z -9.5, q 2e-19, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBX8]] (+0.64, fdr 1e-05), [[BHLHE41]] (+0.63, fdr 7e-06), [[DBP]] (+0.62, fdr 1e-05); moves opposite to [[AVEN]] (-0.58, fdr 2e-05), [[TMEM11-DT]] (-0.58, fdr 2e-05), [[SAP30L-AS1]] (-0.56, fdr 7e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7942.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.73×** | +25.8 | 0e+00 | 45/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **9.40×** | +17.2 | 0e+00 | 49/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.22×** | +9.0 | 5e-17 | 47/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +7.0 | 5e-10 | 31/48 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +6.6 | 5e-09 | 40/48 (RKO, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +6.5 | 9e-09 | 30/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.33×** | +5.5 | 3e-06 | 38/48 (NCI-H1792, SNU-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +4.5 | 4e-04 | 37/49 (A498, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +4.2 | 0.001 | 27/48 (LoVo, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 5 µM |  | **1.65×** | +3.9 | 0.007 | 33/48 (CFPAC-1, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.009 | 26/48 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.009 | 28/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.009 | 24/48 (SNU-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.6 | 0.011 | 26/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.011 | 24/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.019 | 25/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7942.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.299×** | -17.1 | 0e+00 | 43/44 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.389×** | -13.9 | 1e-41 | 44/49 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.456×** | -11.1 | 2e-26 | 46/47 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.495×** | -9.6 | 1e-19 | 43/45 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -9.5 | 2e-19 | 43/48 (A498, SNU-423, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.661×** | -8.2 | 2e-14 | 36/49 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -7.3 | 3e-11 | 40/50 (A498, NCI-H23, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.719×** | -6.8 | 9e-10 | 42/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.683×** | -5.7 | 1e-06 | 38/48 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.708×** | -4.9 | 5e-05 | 31/47 (NCI-H1573, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.729×** | -4.7 | 1e-04 | 29/48 (C32, NCI-H23, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.833×** | -3.7 | 0.009 | 22/48 (A549, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.786×** | -3.4 | 0.031 | 23/48 (C32, NCI-H23, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.808×** | -3.2 | 0.061 | 20/48 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.748×** | -3.1 | 0.078 | 19/48 (A549, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7942. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 214 | 5 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +24.1) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 102 | 6 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.97× (z +33.1) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 139 | 5 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +31.3) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -16.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 114 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -13.7) |
| [[C32 (line)]] | wt | 307 | 1 | 7 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 6.42× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.142× (z -18.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.240× (z -13.8) |
| [[SW48 (line)]] | wt | 237 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -10.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 145 | 2 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +16.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.229× (z -12.6) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 152 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 127 | 2 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -17.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 100 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +19.9) | — |
| [[CFPAC-1 (line)]] | alt | 135 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +23.0) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -13.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 121 | 2 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.45× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -13.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 143 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 125 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.0985× (z -25.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -10.7) |
| [[RKO (line)]] | wt | 81.1 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +21.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.363× (z -9.1) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 140 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -11.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 115 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -10.9) |
| [[SW480 (line)]] | alt | 77.7 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +26.3) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -19.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 81.9 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -16.3) |
| [[HS-578T (line)]] | alt | 96.4 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -12.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 123 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.41× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -9.5) |
| [[LS 180 (line)]] | wt | 114 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +20.0) | — |
| [[NCI-H1792 (line)]] | alt | 137 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 125 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.2× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -15.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 106 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.80× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -10.5) |
| [[A-172 (line)]] | wt | 135 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.3× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.0911× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.420× (z -10.2) |
| [[A549 (line)]] | wt | 92.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +20.3) | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 108 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +16.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -11.8) |
| [[SW 900 (line)]] | alt | 126 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -12.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 96.8 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -11.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 67.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +16.9) | — |
| [[BT-474 (line)]] | alt | 154 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -8.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 139 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -14.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 141 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -13.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 60.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +19.3) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -8.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 132 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -8.9) |
| [[COLO 205 (line)]] | alt | 81.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +18.9) | — |
| [[HepG2_C3A (line)]] | wt | 81.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +16.4) | — |
| [[HOP62 (line)]] | alt | 133 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +12.6) | — |
| [[Hs 766T (line)]] | wt | 97.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -14.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 57.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +21.7) | — |
| [[C-33 A (line)]] | alt | 95.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -10.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 93.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -12.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 116 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0832× (z -9.2) |
| [[SW 1271 (line)]] | alt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7942), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX8]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[BHLHE41]] | +0.63 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[DBP]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[N4BP3]] | +0.62 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[ZNF184]] | +0.62 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[RYBP]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[BCOR]] | +0.61 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[RAB3A]] | +0.61 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[RARA]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[NTHL1]] | +0.58 | +0.50 / +0.37 | both halves | 8e-05 |  |
| [[FOXO6]] | +0.57 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[HPS3]] | +0.56 | +0.44 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | -0.58 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[TMEM11-DT]] | -0.58 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[SAP30L-AS1]] | -0.56 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[EPM2A]] | -0.55 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[ATXN10]] | -0.55 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[NUTM2A-AS1]] | -0.55 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[POU6F1]] | -0.54 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[SLC25A53]] | -0.54 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[MRPS25]] | -0.52 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[PRDM10]] | -0.51 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[NR2C2]] | -0.51 | -0.58 / -0.29 | both halves | 3e-04 |  |
| [[ZNF124]] | -0.51 | -0.38 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MIDEAS's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.373). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.7, -5.7); signed map (-5.0, 15.2). **Vector** length 128, 44.8% of its response variance represented; |z| ≥ 3 in 1,392 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.3 | +6.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.5 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +7.2 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +25.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +17.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.5 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.9 | +4.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +4.4 | +1.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -9.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.3 | +0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.0 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.7 | -0.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.0 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | mitotic deacetylase associated SANT domain protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:73,715,122-73,790,285 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LSR68; previously C14orf117, C14orf43, ELMSAN1 |
| Gene groups (HGNC) | Myb/SANT domain containing; MiDAC complex subunits |
| Matched by | ensembl_id |

UniProt [Q6PJG2](https://www.uniprot.org/uniprotkb/Q6PJG2) carries no function annotation.

**Summary**, from NCBI Gene [91748](https://www.ncbi.nlm.nih.gov/gene/91748):

> Predicted to enable transcription corepressor activity. Involved in chromatin organization. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19853) · Entrez [91748](https://www.ncbi.nlm.nih.gov/gene/91748) · UniProt [Q6PJG2](https://www.uniprot.org/uniprotkb/Q6PJG2) · Ensembl [ENSG00000156030](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156030)

## Data

Gene col 7942: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7942); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7942, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7942]; `tensor/DDL_lfc|DDL_z.npy` [7942]; `embed/gene_vectors.npy` [7942]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7942 or target_col == 7942). Every well: [[MIDEAS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIDEAS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
