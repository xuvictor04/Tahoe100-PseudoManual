---
symbol: "PDE7A"
type: "gene"
col: 12962
ensembl_id: "ENSG00000205268"
name: "phosphodiesterase 7A"
location: "8q13.1"
module: 186
arm: "+"
pooled_cpm: 88.74
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# PDE7A

*phosphodiesterase 7A* — 8q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.52× (z +9.5, q 2e-18, up in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.39× (z +7.4, q 2e-11, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.403× (z -20.5, q 0e+00, down in 43 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.656× (z -9.5, q 3e-19, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDC1]] (+0.68, fdr 7e-06), [[EED]] (+0.68, fdr 7e-06), [[ZMYM2]] (+0.68, fdr 1e-05); moves opposite to [[ZNF655]] (-0.60, fdr 1e-05), [[ZNF776]] (-0.57, fdr 1e-05), [[FCF1]] (-0.57, fdr 2e-05).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SOBP]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Filgotinib (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12962.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.52×** | +9.5 | 2e-18 | 36/47 (A498, AsPC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.43×** | +7.8 | 2e-12 | 34/47 (SW48, NCI-H23, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +7.5 | 1e-11 | 37/47 (A498, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +7.4 | 2e-11 | 32/47 (AsPC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.38×** | +7.2 | 6e-11 | 31/47 (A498, AsPC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +6.8 | 1e-09 | 29/47 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.32×** | +6.0 | 2e-07 | 28/49 (LS 180, SW48, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +5.7 | 9e-07 | 30/48 (AsPC-1, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.26×** | +5.2 | 2e-05 | 25/47 (PANC-1, LoVo, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.17× | +5.0 | 3e-05 | 22/48 (RKO, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.22×** | +4.5 | 4e-04 | 21/47 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.22×** | +4.4 | 5e-04 | 24/47 (A498, AsPC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.20×** | +4.2 | 0.001 | 19/47 (H4, NCI-H460, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.003 | 19/48 (A-427, BT-474, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | 1.19× | +3.8 | 0.006 | 20/46 (LoVo, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.007 | 20/46 (BT-474, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.16× | +3.3 | 0.029 | 15/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift |
| [[venetoclax (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.045 | 12/47 (AsPC-1, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.045 | 16/47 (J82, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.063 | 11/47 (CFPAC-1, J82, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.25×** | +2.9 | 0.068 | 4/47 (HOP62, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.075 | 7/47 (SW480, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12962.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.403×** | -20.5 | 0e+00 | 43/48 (SHP-77, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.423×** | -18.7 | 0e+00 | 39/44 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.530×** | -13.2 | 1e-37 | 39/45 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.656×** | -9.5 | 3e-19 | 33/47 (C32, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.658×** | -9.4 | 4e-19 | 38/47 (C32, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.769×** | -5.9 | 3e-07 | 31/47 (H4, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.787×** | -5.2 | 2e-05 | 27/47 (LOX-IMVI, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.826×** | -4.3 | 0.001 | 25/47 (C32, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -4.1 | 0.003 | 21/47 (C32, NCI-H2347, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.902× | -3.3 | 0.055 | 13/47 (C32, A-427, …) | all doses, flat | low cells (technical?) |
| [[4EGI-1 (drug)]] 5 µM |  | **0.760×** | -3.2 | 0.060 | 16/47 (Hs 766T, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.963× | -3.2 | 0.074 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.862× | -3.1 | 0.081 | 8/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12962. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 136 | 0 | 13 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.327× (z -13.2) |
| [[A498 (line)]] | wt | 105 | 4 (4 ⚠) | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.32× (z +10.9) ⚠ cell-cycle shift, explains ~43% of this change | [[Dinaciclib (drug)]] 5 µM 0.257× (z -17.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 79.5 | 4 (4 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +11.5) ⚠ cell-cycle shift, explains ~55% of this change | [[Dinaciclib (drug)]] 5 µM 0.363× (z -12.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 77.2 | 4 (4 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.9) ⚠ cell-cycle shift, explains ~55% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -9.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 126 | 2 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +11.4) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 5 µM 0.290× (z -17.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 109 | 1 (1 ⚠) | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.14× (z +8.9) ⚠ cell-cycle shift, explains ~43% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -14.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 139 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -9.3) |
| [[SW48 (line)]] | wt | 107 | 2 (2 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +10.6) ⚠ cell-cycle shift, explains ~38% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -13.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 130 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0641× (z -33.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 167 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0849× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -11.1) |
| [[C-33 A (line)]] | alt | 211 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -17.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 85.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.343× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.406× (z -10.9) |
| [[J82 (line)]] | alt | 95.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 92.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +10.2) ⚠ cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -10.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.438× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 78.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 102 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.541× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 70.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -16.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 122 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +13.1) ⚠ cell-cycle shift, explains ~55% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0904× (z -25.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 91.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.374× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.419× (z -8.5) |
| [[A549 (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -12.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 40.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +9.5) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[KATO III (line)]] | alt | 74.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -19.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 80.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -14.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 197 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -21.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 74.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.523× (z -9.7) |
| [[BT-474 (line)]] | alt | 113 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.60× (z +8.9) | — |
| [[H4 (line)]] | wt | 83.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.223× (z -12.3) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 80.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -15.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 84.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -10.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 58.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -8.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 82.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -13.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 65.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -10.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 71.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.369× (z -8.7) |
| [[SNU-1 (line)]] | wt | 96.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -9.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12962), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDC1]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[EED]] | +0.68 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[ZMYM2]] | +0.68 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[PPP2R5E]] | +0.67 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[TENT4A]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PDXP]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[C6orf136]] | +0.64 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[SAMD1]] | +0.63 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[CABIN1]] | +0.62 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[NUDT1]] | +0.61 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TBC1D12]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[BMPR1A]] | +0.61 | +0.67 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF655]] | -0.60 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[ZNF776]] | -0.57 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[FCF1]] | -0.57 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[ZBED9]] | -0.57 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[PSORS1C1]] | -0.56 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[ZNF701]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[CHMP4B]] | -0.56 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[LINC00486]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[MDM4]] | -0.55 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[SLC22A1]] | -0.54 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | -0.54 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[VCPIP1]] | -0.53 | -0.57 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOBP]] | B | SOBP activity raises PDE7A's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.59× lower at baseline in the lines without SOBP | 0.003 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[P3H3]] | B | P3H3 activity raises PDE7A's level | lines that do not express P3H3 (10) vs lines expressing it (40) | 1.58× lower at baseline in the lines without P3H3 | 0.017 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |
| [[LEF1]] | B | LEF1 activity raises PDE7A's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 1.30× lower at baseline in the lines without LEF1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Filgotinib (drug)]] 0.05 µM | C | PDE7A's natural level raises the cells' numbers under Filgotinib 0.05 µM (protects the cells) | PDE7A's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.310 over the table, 0.060 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.799). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.6, -18.1); signed map (-42.5, 18.3). **Vector** length 119, 34.8% of its response variance represented; |z| ≥ 3 in 1,144 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.2 | +7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.2 | +6.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.0 | +6.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | +4.0 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +7.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.7 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +5.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.6 | +2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.3 | -9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.2 | -9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.6 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -4.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.1 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -0.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 7A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.1 — chr8:65,714,334-65,842,322 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCP1 |
| Gene groups (HGNC) | Phosphodiesterases |
| Reactome | 3 pathways, smallest: G alpha (s) signalling events; GPCR downstream signalling; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13946](https://www.uniprot.org/uniprotkb/Q13946) (High affinity 3',5'-cyclic-AMP phosphodiesterase 7A):

> Hydrolyzes the second messenger cAMP, which is a key regulator of many important physiological processes. May have a role in muscle signal transduction.

**Summary**, from NCBI Gene [5150](https://www.ncbi.nlm.nih.gov/gene/5150):

> The protein encoded by this gene belongs to the cyclic nucleotide phosphodiesterase (PDE) family, and PDE7 subfamily. This PDE hydrolyzes the second messenger, cAMP, which is a regulator and mediator of a number of cellular responses to extracellular signals. Thus, by regulating the cellular concentration of cAMP, this protein plays a key role in many important physiological processes. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. …

**Accessions** — [HGNC:8791](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8791) · Entrez [5150](https://www.ncbi.nlm.nih.gov/gene/5150) · UniProt [Q13946](https://www.uniprot.org/uniprotkb/Q13946) · Ensembl [ENSG00000205268](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205268)

## Data

Gene col 12962: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12962); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12962, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12962]; `tensor/DDL_lfc|DDL_z.npy` [12962]; `embed/gene_vectors.npy` [12962]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12962 or target_col == 12962). Every well: [[PDE7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
