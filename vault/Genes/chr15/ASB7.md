---
symbol: "ASB7"
type: "gene"
col: 11406
ensembl_id: "ENSG00000183475"
name: "ankyrin repeat and SOCS box containing 7"
location: "15q26.3"
module: 178
arm: "+"
pooled_cpm: 34.91
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# ASB7

*ankyrin repeat and SOCS box containing 7* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.38× (z +15.6, q 0e+00, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.317× (z -23.2, q 0e+00, down in 45 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.574× (z -10.8, q 5e-25, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHDC10]] (+0.81, fdr 7e-06), [[NDUFAF7]] (+0.78, fdr 7e-06), [[KIAA2013]] (+0.74, fdr 7e-06); moves opposite to [[THOC6]] (-0.68, fdr 7e-06), [[TNFRSF12A]] (-0.65, fdr 7e-06), [[SKIL]] (-0.65, fdr 7e-06).
> It is in [[Module 178]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[THBS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11406.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.38×** | +15.6 | 0e+00 | 43/49 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +12.5 | 4e-33 | 39/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.01×** | +11.6 | 6e-29 | 38/48 (SW480, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.44×** | +7.4 | 2e-11 | 31/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +6.2 | 8e-08 | 25/47 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.9 | 5e-07 | 23/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +5.7 | 8e-07 | 24/48 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.34×** | +5.6 | 1e-06 | 25/48 (PANC-1, AN3 CA, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **1.61×** | +5.0 | 3e-05 | 18/47 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **1.27×** | +4.7 | 2e-04 | 20/47 (SW480, HepG2/C3A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +4.3 | 9e-04 | 18/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.2 | 0.001 | 16/35 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.1 | 0.001 | 13/43 (NCI-H1792, J82, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.1 | 0.002 | 19/47 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.002 | 12/48 (HOP62, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.005 | 17/48 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.1 | 0.050 | 11/48 (C32, J82, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.050 | 14/48 (HEC-1-A, LOX-IMVI, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.17× | +3.0 | 0.069 | 8/47 (Panc 03.27, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11406.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.317×** | -23.2 | 0e+00 | 45/46 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.425×** | -16.6 | 0e+00 | 34/38 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.640×** | -12.7 | 7e-35 | 38/48 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.530×** | -11.9 | 3e-30 | 31/42 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.574×** | -10.8 | 5e-25 | 31/48 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.623×** | -9.6 | 1e-19 | 31/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.636×** | -9.1 | 6e-18 | 34/47 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -4.6 | 3e-04 | 20/48 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.813×** | -4.0 | 0.004 | 16/48 (LS 180, NCI-H2347, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.873× | -3.9 | 0.006 | 13/48 (SW 1088, NCI-H661, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.827×** | -3.8 | 0.006 | 13/48 (RPMI-7951, NCI-H1573, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.826×** | -3.7 | 0.009 | 15/47 (LOX-IMVI, H4, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.833× | -3.7 | 0.010 | 10/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.847× | -3.4 | 0.032 | 9/48 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.849× | -3.3 | 0.034 | 9/48 (Panc 03.27, LS 180, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.850× | -3.3 | 0.035 | 7/48 (LS 180, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.851× | -3.3 | 0.037 | 17/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.854× | -3.2 | 0.043 | 8/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.860× | -3.0 | 0.065 | 5/48 (SW 1088, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11406. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 50.2 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -14.4) |
| [[KATO III (line)]] | alt | 48.4 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.41× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.346× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 50.1 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.332× (z -10.7) |
| [[HOP62 (line)]] | alt | 43.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.335× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 44.1 | 2 | 3 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.30× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -11.5) |
| [[SW480 (line)]] | alt | 39.2 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.79× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -13.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 45.8 | 0 | 4 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0695× (z -11.8) |
| [[HT-29 (line)]] | alt | 52.5 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.87× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -11.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 33.1 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.65× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -11.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 26.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 21.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -9.0) |
| [[COLO 205 (line)]] | alt | 40.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -16.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.187× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 27.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0792× (z -18.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 39.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -13.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 36.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -13.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -8.6) |
| [[A498 (line)]] | wt | 34.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -9.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 32.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -13.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 35.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -11.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 31.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -11.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 34.0 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.99× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 7.97× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 37.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.09× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -9.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 41.9 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 5 µM 0.0638× (z -10.5) ⚠ toxic |
| [[A549 (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -10.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -8.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -12.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -11.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 34.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.85× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -10.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -15.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -8.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -11.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11406), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHDC10]] | +0.81 | +0.80 / +0.81 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.78 | +0.70 / +0.80 | both halves | 7e-06 |  |
| [[KIAA2013]] | +0.74 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[RELCH]] | +0.74 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[TTC9C]] | +0.72 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.72 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[BMT2]] | +0.72 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[NENF]] | +0.71 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[C12orf76]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[CWC15]] | +0.70 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[NUDT2]] | +0.70 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[ATPAF2]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[TNFRSF12A]] | -0.65 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[SKIL]] | -0.65 | -0.61 / -0.68 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[WDR1]] | -0.64 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[FKRP]] | -0.63 | -0.71 / -0.60 | both halves | 7e-06 |  |
| [[TMEM185B]] | -0.62 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[KPNA4]] | -0.62 | -0.47 / -0.70 | both halves | 2e-05 |  |
| [[ZYX]] | -0.61 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[MYO1C]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.61 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[CSRP1]] | -0.60 | -0.50 / -0.68 | both halves | 1e-05 |  |
| [[CELSR3]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THBS1]] | B | THBS1 activity raises ASB7's level | lines that do not express THBS1 (14) vs lines expressing it (36) | 1.10× lower at baseline in the lines without THBS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ETNK2, SLC35G2, ENSG00000176593 |
| [[ARC]] | B | ARC activity raises ASB7's level | lines that do not express ARC (19) vs lines expressing it (31) | 1.16× lower at baseline in the lines without ARC | 0.059 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |
| [[ISY1]] | C | ISY1's natural level strengthens ASB7's drug response | ISY1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.03; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.892). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.5, -13.4); signed map (-34.5, -8.1). **Vector** length 122, 33.6% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.2 | +12.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.9 | +15.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.0 | +11.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.0 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.0 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -10.3 | -12.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.5 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.1 | -9.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.1 | -9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | -23.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -3.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.4 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and SOCS box containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:100,602,589-100,651,701 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H672](https://www.uniprot.org/uniprotkb/Q9H672) (Ankyrin repeat and SOCS box protein 7):

> Substrate-recognition component of a cullin-5-RING E3 ubiquitin-protein ligase complex (ECS complex, also named CRL5 complex), which mediates the ubiquitination and subsequent proteasomal degradation of target proteins, such as LZTS1, PSRC1 and SUV39H1. The ECS(ASB7) complex acts as a negative regulator of H3K9me3 histone mark by mediating ubiquitination and degradation of SUV39H1: ASB7 is recruited to heterochromatin by CBX5 (HP1 alpha), where it associates with SUV39H1, promoting the …

**Summary**, from NCBI Gene [140460](https://www.ncbi.nlm.nih.gov/gene/140460):

> The protein encoded by this gene belongs to a family of ankyrin repeat proteins that, along with four other protein families, contains a C-terminal SOCS box motif. Growing evidence suggests that the SOCS box acts as a bridge between specific substrate-binding domains and the more generic proteins that comprise a large family of E3 ubiquitin protein ligases. In this way, SOCS box containing proteins may regulate protein turnover by targeting proteins for polyubiquination and, therefore, for …

**Accessions** — [HGNC:17182](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17182) · Entrez [140460](https://www.ncbi.nlm.nih.gov/gene/140460) · UniProt [Q9H672](https://www.uniprot.org/uniprotkb/Q9H672) · Ensembl [ENSG00000183475](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183475)

## Data

Gene col 11406: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11406); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11406, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11406]; `tensor/DDL_lfc|DDL_z.npy` [11406]; `embed/gene_vectors.npy` [11406]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11406 or target_col == 11406). Every well: [[ASB7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASB7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
