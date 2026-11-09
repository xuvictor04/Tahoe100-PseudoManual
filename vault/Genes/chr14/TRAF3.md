---
symbol: "TRAF3"
type: "gene"
col: 5192
ensembl_id: "ENSG00000131323"
name: "TNF receptor associated factor 3"
location: "14q32.32"
module: 1
arm: "+"
pooled_cpm: 144.87
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 15
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TRAF3

*TNF receptor associated factor 3* — 14q32.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.83× (z +31.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.447× (z -17.4, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCSK6]] (+0.60, fdr 2e-05), [[GRIP1]] (+0.58, fdr 5e-05), [[PALD1]] (+0.58, fdr 1e-05); moves opposite to [[IFT172]] (-0.59, fdr 3e-05), [[PPP1R12B]] (-0.57, fdr 4e-05), [[PLAG1]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SLC16A9]] → it (grade B ⚠); 1 goes from it, the strongest it → [[IFT172]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5192.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.83×** | +31.9 | 0e+00 | 47/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +14.6 | 0e+00 | 44/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +10.9 | 2e-25 | 40/48 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +7.9 | 3e-13 | 40/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +7.9 | 3e-13 | 33/48 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +7.5 | 7e-12 | 26/49 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +7.4 | 1e-11 | 32/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +7.3 | 2e-11 | 33/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +5.5 | 3e-06 | 29/48 (NCI-H460, HT-29, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +5.4 | 3e-06 | 26/48 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.71×** | +5.3 | 5e-06 | 28/49 (BT-474, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +4.9 | 6e-05 | 27/48 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 2e-04 | 23/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.5 | 3e-04 | 24/48 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.011 | 21/48 (Hs 766T, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 5 µM |  | 1.17× | +3.3 | 0.031 | 17/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.088 | 12/49 (NCI-H460, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5192.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.447×** | -17.4 | 0e+00 | 42/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.529×** | -13.8 | 7e-41 | 41/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -11.6 | 8e-29 | 36/44 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.589×** | -11.5 | 2e-28 | 40/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.632×** | -9.9 | 3e-21 | 35/49 (SW48, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.510×** | -6.7 | 1e-09 | 41/47 (BT-474, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.733×** | -6.7 | 1e-09 | 37/49 (KATO III, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.777×** | -5.5 | 3e-06 | 30/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~6% of this change | **0.819×** | -4.3 | 1e-03 | 24/48 (J82, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.821×** | -4.3 | 0.001 | 23/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.819×** | -4.2 | 0.002 | 24/47 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.813×** | -4.1 | 0.002 | 21/45 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.751×** | -3.7 | 0.009 | 24/48 (J82, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.845× | -3.6 | 0.011 | 20/48 (KATO III, CHP-212, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.846× | -3.6 | 0.012 | 18/48 (LOX-IMVI, hTERT-HPNE, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.766×** | -3.5 | 0.018 | 21/48 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.901× | -3.1 | 0.056 | 6/49 (SK-MEL-2, NCI-H1573, …) | all doses, flat |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.863× | -3.1 | 0.059 | 13/49 (KATO III, NCI-H2347, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.873× | -2.9 | 0.085 | 17/48 (SW 1088, A498, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.909× | -2.9 | 0.085 | 10/48 (H4, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5192. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 128 | 8 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +28.9) | [[Panobinostat (drug)]] 0.5 µM 0.440× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 107 | 9 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +29.0) | [[Panobinostat (drug)]] 0.5 µM 0.487× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 238 | 2 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.363× (z -13.7) |
| [[BT-474 (line)]] | alt | 117 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -11.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 167 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +16.7) | [[Panobinostat (drug)]] 5 µM 0.172× (z -21.9) |
| [[NCI-H1573 (line)]] | alt | 239 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -13.1) |
| [[SNU-1 (line)]] | wt | 209 | 3 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.391× (z -11.2) |
| [[A-427 (line)]] | wt | 160 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +18.3) | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -18.7) |
| [[LOX-IMVI (line)]] | wt | 189 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -14.1) |
| [[NCI-H2347 (line)]] | alt | 189 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +26.4) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -13.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 245 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -20.5) |
| [[SK-MEL-2 (line)]] | alt | 161 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +25.7) | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -17.5) |
| [[SW1417 (line)]] | alt | 150 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +21.0) | [[Panobinostat (drug)]] 0.5 µM 0.413× (z -12.9) |
| [[SW480 (line)]] | alt | 139 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +14.6) | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -19.9) |
| [[HEC-1-A (line)]] | alt | 190 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +18.8) | [[Panobinostat (drug)]] 0.5 µM 0.387× (z -14.6) |
| [[J82 (line)]] | alt | 185 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +15.9) | [[Panobinostat (drug)]] 0.5 µM 0.424× (z -13.1) |
| [[SW48 (line)]] | wt | 400 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.262× (z -15.7) |
| [[A549 (line)]] | wt | 204 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.358× (z -13.8) |
| [[LoVo (line)]] | wt | 139 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +18.8) | [[Panobinostat (drug)]] 0.5 µM 0.467× (z -10.3) |
| [[PANC-1 (line)]] | alt | 142 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +23.8) | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -16.9) |
| [[AsPC-1 (line)]] | alt | 136 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.423× (z -9.5) |
| [[C-33 A (line)]] | alt | 192 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -14.8) |
| [[C32 (line)]] | wt | 194 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -14.0) |
| [[HepG2_C3A (line)]] | wt | 101 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +19.2) | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -10.4) |
| [[Hs 766T (line)]] | wt | 89.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +20.5) | — |
| [[NCI-H23 (line)]] | alt | 111 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -17.6) |
| [[RPMI-7951 (line)]] | alt | 99.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.67× (z +24.2) | — |
| [[SW 900 (line)]] | alt | 126 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +20.9) | — |
| [[A-172 (line)]] | wt | 97.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.468× (z -9.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 209 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 136 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +26.5) | — |
| [[HT-29 (line)]] | alt | 62.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +23.3) | — |
| [[NCI-H1792 (line)]] | alt | 138 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +22.0) | [[Dinaciclib (drug)]] 5 µM 0.463× (z -9.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 213 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -11.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 62.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +13.4) | — |
| [[H4 (line)]] | wt | 90.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +21.5) | — |
| [[HS-578T (line)]] | alt | 80.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +22.7) | — |
| [[hTERT-HPNE (line)]] | wt | 105 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +12.3) | — |
| [[KATO III (line)]] | alt | 68.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +19.2) | — |
| [[CHP-212 (line)]] | wt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +12.6) | — |
| [[HCT15 (line)]] | alt | 124 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +14.0) | — |
| [[LS 180 (line)]] | wt | 102 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.490× (z -8.5) |
| [[SHP-77 (line)]] | alt | 75.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +15.7) | — |
| [[SNU-423 (line)]] | alt | 74.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +18.9) | — |
| [[SW 1271 (line)]] | alt | 177 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.159× (z -10.1) |
| [[A498 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5192), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCSK6]] | +0.60 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[GRIP1]] | +0.58 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[PALD1]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SMCO2]] | +0.57 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[IL34]] | +0.57 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[KCNQ4]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[NANOS3]] | +0.56 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[CGAS]] | +0.56 | +0.45 / +0.44 | both halves | 3e-05 | STRING 528 |
| [[WNT3]] | +0.56 | +0.46 / +0.36 | both halves | 1e-04 |  |
| [[ICA1L]] | +0.56 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[E2F3]] | +0.55 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[PRKAR1B]] | +0.55 | +0.59 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT172]] | -0.59 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[PPP1R12B]] | -0.57 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[PLAG1]] | -0.56 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[PLD3]] | -0.55 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ALDH6A1]] | -0.53 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[OS9]] | -0.52 | -0.53 / -0.43 | both halves | 4e-05 |  |
| [[PRUNE1]] | -0.52 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[MED23]] | -0.52 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[RAB2A]] | -0.51 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[ATP5F1C]] | -0.51 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[RAB40B]] | -0.51 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[TMEM245]] | -0.50 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A9]] | B | SLC16A9 activity raises TRAF3's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 1.19× lower at baseline in the lines without SLC16A9 | 0.041 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |
| [[SPHK1]] | B | SPHK1 activity raises TRAF3's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 1.28× lower at baseline in the lines without SPHK1 | 0.055 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[PIK3CA]] | B | PIK3CA activity raises TRAF3's level | compounds that target PIK3CA: 3 of 4 lower it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[FAM169A]] | B | FAM169A activity raises TRAF3's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.32× lower at baseline in the lines without FAM169A | 0.078 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[SUGCT]] | C | SUGCT activity raises TRAF3's level | lines that do not express SUGCT (4) vs lines expressing it (46) | 2.01× lower at baseline in the lines without SUGCT | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, CABYR, HHAT; maybe low, not absent; its own permutation p |
| [[NKAIN1]] | C | NKAIN1 activity raises TRAF3's level | lines that do not express NKAIN1 (4) vs lines expressing it (46) | 1.94× lower at baseline in the lines without NKAIN1 | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFT172]] | C | TRAF3's natural level weakens IFT172's drug response | TRAF3's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.43; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.288). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (14.1, 1.6); signed map (23.2, 5.8). **Vector** length 117, 39.0% of its response variance represented; |z| ≥ 3 in 1,372 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +31.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +14.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +10.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +3.0 |
| fall | [[NG25 (drug)]] 5 µM |  | -7.0 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.7 | -17.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.1 | -11.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.1 | +1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -5.1 | -6.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.7 | -1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.3 | -3.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor associated factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.32 — chr14:102,777,449-102,911,500 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAP-1, CD40bp, CRAF1, LAP1, RNF118 |
| Gene groups (HGNC) | Ring finger proteins; TNF receptor associated factors; Zinc fingers TRAF-type; RING finger E3 ubiquitin protein ligases |
| Reactome | 29 pathways, smallest: TRAF3 deficiency - HSE; Regulation of TBK1, IKKε-mediated activation of IRF3, IRF7 upon TLR3 ligation; Regulation of TBK1, IKKε (IKBKE)-mediated activation of IRF3, IRF7 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13114](https://www.uniprot.org/uniprotkb/Q13114) (TNF receptor-associated factor 3):

> Cytoplasmic E3 ubiquitin ligase that regulates various signaling pathways, such as the NF-kappa-B, mitogen-activated protein kinase (MAPK) and interferon regulatory factor (IRF) pathways, and thus controls a lot of biological processes in both immune and non-immune cell types. In TLR and RLR signaling pathways, acts as an E3 ubiquitin ligase promoting the synthesis of 'Lys-63'-linked polyubiquitin chains on several substrates such as ASC that lead to the activation of the type I interferon …

**Summary**, from NCBI Gene [7187](https://www.ncbi.nlm.nih.gov/gene/7187):

> The protein encoded by this gene is a member of the TNF receptor associated factor (TRAF) protein family. TRAF proteins associate with, and mediate the signal transduction from, members of the TNF receptor (TNFR) superfamily. This protein participates in the signal transduction of CD40, a TNFR family member important for the activation of the immune response. This protein is found to be a critical component of the lymphotoxin-beta receptor (LTbetaR) signaling complex, which induces NF-kappaB …

**Accessions** — [HGNC:12033](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12033) · Entrez [7187](https://www.ncbi.nlm.nih.gov/gene/7187) · UniProt [Q13114](https://www.uniprot.org/uniprotkb/Q13114) · Ensembl [ENSG00000131323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131323)

## Data

Gene col 5192: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5192); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5192, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5192]; `tensor/DDL_lfc|DDL_z.npy` [5192]; `embed/gene_vectors.npy` [5192]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5192 or target_col == 5192). Every well: [[TRAF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
