---
symbol: "MTM1"
type: "gene"
col: 10049
ensembl_id: "ENSG00000171100"
name: "myotubularin 1"
location: "Xq28"
module: 54
arm: "+"
pooled_cpm: 41.11
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# MTM1

*myotubularin 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.07× (z +16.0, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.382× (z -21.2, q 0e+00, down in 40 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.539× (z -13.6, q 5e-40, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEBP1]] (+0.69, fdr 7e-06), [[ZFYVE21]] (+0.67, fdr 3e-05), [[PTPRA]] (+0.65, fdr 1e-05); moves opposite to [[C22orf46]] (-0.66, fdr 9e-06), [[SRSF10]] (-0.65, fdr 1e-05), [[SRSF1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10049.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.07×** | +16.0 | 0e+00 | 46/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +15.7 | 0e+00 | 47/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.02×** | +14.8 | 0e+00 | 45/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +8.3 | 1e-14 | 27/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +7.6 | 4e-12 | 30/47 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +5.4 | 6e-06 | 19/48 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.25×** | +4.6 | 3e-04 | 19/48 (SNU-423, HT-29, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.5 | 5e-04 | 20/48 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +4.3 | 0.001 | 21/48 (SNU-423, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.24×** | +4.3 | 0.001 | 14/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.004 | 20/47 (SW480, A-427, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.9 | 0.004 | 11/48 (SW 900, CFPAC-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.19× | +3.7 | 0.010 | 14/47 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.5 | 0.019 | 9/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.11× | +3.3 | 0.032 | 5/48 (SNU-423, SW 900, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.033 | 8/47 (SW480, AsPC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.061 | 10/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.077 | 8/47 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.10× | +3.0 | 0.081 | 7/48 (SW480, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10049.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.382×** | -21.2 | 0e+00 | 40/45 (Panc 03.27, A-172, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.428×** | -17.3 | 0e+00 | 37/39 (A-172, SW1417, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.446×** | -17.1 | 0e+00 | 32/38 (NCI-H460, KATO III, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.539×** | -13.6 | 5e-40 | 38/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.647×** | -9.2 | 3e-18 | 34/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.404×** | -8.9 | 6e-17 | 37/49 (A549, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.774×** | -8.0 | 1e-13 | 28/47 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.706×** | -7.7 | 1e-12 | 29/47 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **0.749×** | -6.4 | 1e-08 | 24/45 (KATO III, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.773×** | -5.7 | 8e-07 | 28/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.782×** | -5.2 | 1e-05 | 24/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.600×** | -5.0 | 3e-05 | 18/47 (hTERT-HPNE, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.847× | -3.7 | 0.011 | 19/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.844× | -3.6 | 0.014 | 13/48 (AsPC-1, SW480, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | 0.900× | -3.3 | 0.038 | 8/48 (SW1417, SNU-423, …) | rises with dose |  |
| [[Mebendazole (drug)]] 0.5 µM |  | 0.866× | -3.2 | 0.055 | 6/48 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.867× | -3.1 | 0.055 | 9/47 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.865× | -3.0 | 0.073 | 12/48 (AN3 CA, Panc 03.27, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.874× | -3.0 | 0.089 | 8/48 (HepG2/C3A, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10049. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.7 | 2 | 13 (13 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.0662× (z -30.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 52.4 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.00× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.388× (z -10.0) |
| [[SW480 (line)]] | alt | 47.7 | 4 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.31× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -11.7) |
| [[PANC-1 (line)]] | alt | 62.3 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.41× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -17.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 51.5 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -11.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 47.3 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -13.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 54.7 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0613× (z -26.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 34.0 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -12.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 20.5 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.28× (z +9.5) | [[Auranofin (drug)]] 5 µM 0.236× (z -12.0) |
| [[HT-29 (line)]] | alt | 47.0 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.63× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.271× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 49.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 54.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.269× (z -14.0) |
| [[A-427 (line)]] | wt | 40.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.49× (z +14.2) ⚠ cell-cycle shift, explains ~64% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -8.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 37.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -16.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 23.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.152× (z -14.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 45.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -16.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 39.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -9.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 54.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -23.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 61.5 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.35× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -15.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 25.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.163× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[HS-578T (line)]] | alt | 27.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -12.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 32.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.310× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[LOX-IMVI (line)]] | wt | 31.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0594× (z -23.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 22.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 51.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.325× (z -10.3) |
| [[SHP-77 (line)]] | alt | 29.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -14.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 42.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -12.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 28.2 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.106× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 57.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -11.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -12.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 45.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -13.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 44.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0725× (z -17.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 48.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0404× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[RPMI-7951 (line)]] | alt | 34.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.250× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 55.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -11.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.145× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10049), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEBP1]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ZFYVE21]] | +0.67 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[PTPRA]] | +0.65 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[HSDL1]] | +0.65 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[GIT1]] | +0.64 | +0.37 / +0.68 | both halves | 8e-05 |  |
| [[CBFA2T2]] | +0.63 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CNIH4]] | +0.62 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[GNB2]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[TRIM62]] | +0.62 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[TMEM50B]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[DUSP18]] | +0.62 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[RNF38]] | +0.62 | +0.46 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C22orf46]] | -0.66 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[SRSF10]] | -0.65 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[SRSF1]] | -0.65 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[SRSF6]] | -0.64 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[ZNF655]] | -0.64 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.63 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[NCR3LG1]] | -0.63 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[THOC6]] | -0.63 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[TASOR]] | -0.61 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[FNBP1P1]] | -0.60 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ZNF121]] | -0.60 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[NANOS3]] | -0.59 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RP1]] | B | RP1 activity raises MTM1's level | lines that do not express RP1 (19) vs lines expressing it (31) | 1.45× lower at baseline in the lines without RP1 | 0.015 | ⚠ within organs, on part of the lines; also absent: CYB5R2, KIAA1549L, KCNN4; maybe low, not absent |
| [[PPP1R3B-DT]] | B | PPP1R3B-DT activity raises MTM1's level | lines that do not express PPP1R3B-DT (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without PPP1R3B-DT | 0.060 | ⚠ within organs, on part of the lines; also absent: KNDC1; maybe low, not absent; its own permutation p |
| [[TOP2A]] | B | TOP2A activity lowers MTM1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.498). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-1.3, -21.2); signed map (-25.1, 5.4). **Vector** length 89.3, 21.5% of its response variance represented; |z| ≥ 3 in 1,151 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.9 | +15.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +14.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +16.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +2.8 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.0 | +1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +0.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.1 | -13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.8 | -17.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -6.3 | -8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -17.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.4 | -21.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | myotubularin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:150,568,417-150,673,143 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Myotubularins; Phosphoinositide phosphatases |
| Reactome | 6 pathways, smallest: Synthesis of PIPs at the late endosome membrane; Synthesis of PIPs at the early endosome membrane; Synthesis of PIPs at the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13496](https://www.uniprot.org/uniprotkb/Q13496) (Myotubularin):

> Lipid phosphatase which dephosphorylates phosphatidylinositol 3-monophosphate (PI3P) and phosphatidylinositol 3,5-bisphosphate (PI(3,5)P2). Has also been shown to dephosphorylate phosphotyrosine- and phosphoserine-containing peptides. Negatively regulates EGFR degradation through regulation of EGFR trafficking from the late endosome to the lysosome. Plays a role in vacuolar formation and morphology. Regulates desmin intermediate filament assembly and architecture. Plays a role in mitochondrial …

**Summary**, from NCBI Gene [4534](https://www.ncbi.nlm.nih.gov/gene/4534):

> This gene encodes a dual-specificity phosphatase that acts on both phosphotyrosine and phosphoserine. It is required for muscle cell differentiation and mutations in this gene have been identified as being responsible for X-linked myotubular myopathy. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7448](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7448) · Entrez [4534](https://www.ncbi.nlm.nih.gov/gene/4534) · UniProt [Q13496](https://www.uniprot.org/uniprotkb/Q13496) · Ensembl [ENSG00000171100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171100)

## Data

Gene col 10049: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10049); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10049, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10049]; `tensor/DDL_lfc|DDL_z.npy` [10049]; `embed/gene_vectors.npy` [10049]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10049 or target_col == 10049). Every well: [[MTM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
