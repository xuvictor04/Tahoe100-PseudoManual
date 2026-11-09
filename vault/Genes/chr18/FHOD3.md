---
symbol: "FHOD3"
type: "gene"
col: 5603
ensembl_id: "ENSG00000134775"
name: "formin homology 2 domain containing 3"
location: "18q12.2"
module: 193
arm: "+"
pooled_cpm: 83.78
n_lines_expressing: 36
n_dd_up: 19
n_dd_down: 24
n_dd_up_clean: 12
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 8
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# FHOD3

*formin homology 2 domain containing 3* — 18q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.47× (z +8.5, q 1e-14, up in 24 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.487× (z -15.9, q 0e+00, down in 28 of 34 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.431× (z -13.2, q 3e-37, down in 27 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FMNL2]] (+0.56, fdr 1e-05), [[GRB14]] (+0.55, fdr 3e-05), [[CDYL]] (+0.55, fdr 1e-05); moves opposite to [[COPZ1]] (-0.50, fdr 4e-05), [[ZNF547]] (-0.47, fdr 8e-05), [[CENPBD2P]] (-0.46, fdr 3e-04).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ESYT3]] → it (grade B ⚠); 8 go from it, the strongest it → [[ROR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5603.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +8.5 | 1e-14 | 24/34 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.55×** | +6.6 | 1e-08 | 26/34 (NCI-H2347, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +6.2 | 1e-07 | 18/34 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 2e-05 | 20/34 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.39×** | +5.2 | 2e-05 | 21/35 (LoVo, C-33 A, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.25×** | +4.9 | 9e-05 | 18/34 (A498, NCI-H23, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.5 | 5e-04 | 19/34 (RPMI-7951, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.33×** | +4.5 | 6e-04 | 16/34 (CFPAC-1, H4, …) | all doses, flat |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.31×** | +4.2 | 0.002 | 16/34 (SNU-423, hTERT-HPNE, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.28×** | +3.8 | 0.008 | 15/34 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +3.7 | 0.011 | 13/35 (LoVo, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.015 | 15/34 (NCI-H1573, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.018 | 14/35 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +3.3 | 0.040 | 15/34 (SNU-423, J82, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.040 | 13/34 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.063 | 11/34 (Panc 03.27, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.092 | 11/34 (NCI-H2347, HOP62, …) | two highest doses |  |
| [[Dabrafenib (drug)]] 5 µM |  | **1.44×** | +3.0 | 0.092 | 15/35 (NCI-H460, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5603.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.487×** | -15.9 | 0e+00 | 28/34 (A549, NCI-H2030, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.431×** | -13.2 | 3e-37 | 27/34 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.473×** | -10.1 | 8e-22 | 27/34 (AN3 CA, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.533×** | -9.9 | 9e-21 | 26/34 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.547×** | -9.4 | 4e-19 | 23/34 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.558×** | -8.8 | 2e-16 | 21/31 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.561×** | -8.7 | 3e-16 | 27/33 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.575×** | -8.7 | 3e-16 | 24/33 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.608×** | -7.2 | 3e-11 | 20/32 (J82, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.708×** | -5.2 | 1e-05 | 21/34 (A549, SK-MEL-2, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.727×** | -5.0 | 3e-05 | 21/33 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.726×** | -4.7 | 1e-04 | 20/34 (Panc 03.27, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.576×** | -4.5 | 3e-04 | 18/35 (A549, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **0.755×** | -4.4 | 5e-04 | 18/33 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.761×** | -4.3 | 7e-04 | 20/34 (A498, SK-MEL-2, …) | two highest doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.780×** | -3.7 | 0.006 | 15/34 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.788×** | -3.7 | 0.006 | 16/35 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.814×** | -3.6 | 0.008 | 16/34 (NCI-H1573, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.859× | -3.4 | 0.021 | 12/34 (A549, SNU-423, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.845× | -3.3 | 0.029 | 14/34 (J82, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.818×** | -3.2 | 0.037 | 16/33 (SW1417, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 5 µM |  | 0.871× | -3.1 | 0.049 | 4/35 (Panc 03.27, SNU-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.689×** | -3.1 | 0.049 | 16/34 (AN3 CA, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.830×** | -2.9 | 0.071 | 15/34 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5603. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 128 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0423× (z -39.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0801× (z -22.1) |
| [[NCI-H460 (line)]] | wt | 88.4 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -22.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -15.6) |
| [[LoVo (line)]] | wt | 39.7 | 4 (2 ⚠) | 6 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.45× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -13.5) |
| [[PANC-1 (line)]] | alt | 200 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -19.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -19.4) |
| [[SK-MEL-2 (line)]] | alt | 208 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -26.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.221× (z -15.4) |
| [[J82 (line)]] | alt | 179 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -12.9) |
| [[AN3 CA (line)]] | alt | 197 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0769× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0578× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 143 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -29.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -15.5) |
| [[NCI-H23 (line)]] | alt | 101 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -20.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.359× (z -10.2) |
| [[SNU-1 (line)]] | wt | 52.4 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -13.4) |
| [[SNU-423 (line)]] | alt | 221 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -23.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.371× (z -8.6) |
| [[A-172 (line)]] | wt | 93.4 | 2 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.01× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -13.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -11.6) |
| [[A498 (line)]] | wt | 105 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -15.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 153 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.470× (z -9.2) |
| [[SW480 (line)]] | alt | 69.0 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.345× (z -12.7) |
| [[A-427 (line)]] | wt | 90.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.440× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 116 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.352× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 322 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -18.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RPMI-7951 (line)]] | alt | 124 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -10.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -8.6) |
| [[C-33 A (line)]] | alt | 111 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.00× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -12.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 50.0 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.65× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -8.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H1573 (line)]] | alt | 29.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 78.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.41× (z +12.2) | — |
| [[SW1417 (line)]] | alt | 48.9 | 1 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 2.40× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -9.7) |
| [[HS-578T (line)]] | alt | 49.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.91× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 67.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -10.2) |
| [[NCI-H596 (line)]] | alt | 66.0 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.116× (z -19.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.35 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.85 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.30 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.30 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.53 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.87 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.44 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5603), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FMNL2]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 | same gene group |
| [[GRB14]] | +0.55 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[CDYL]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[CDH4]] | +0.55 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[ROR1]] | +0.54 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[SRPK1]] | +0.53 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[ANKRD44]] | +0.53 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[SHANK2]] | +0.53 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[THSD4]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[MCOLN2]] | +0.51 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[DOCK4]] | +0.51 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[TARBP1]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPZ1]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ZNF547]] | -0.47 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[CENPBD2P]] | -0.46 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[KLC4]] | -0.45 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[TMEM91]] | -0.45 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[NOL3]] | -0.45 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[OSCP1]] | -0.45 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[ARMCX3]] | -0.44 | -0.57 / -0.26 | both halves | 3e-04 |  |
| [[DAZAP2]] | -0.44 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[TMF1]] | -0.44 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[DNAJB4]] | -0.43 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[GOLGA2]] | -0.43 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESYT3]] | B | ESYT3 activity raises FHOD3's level | lines that do not express ESYT3 (15) vs lines expressing it (35) | 2.92× lower at baseline in the lines without ESYT3 | 0.015 | ⚠ within organs, on part of the lines; also absent: BEND6, ENSG00000224905, ZNF354C; maybe low, not absent |
| [[BCAR3]] | B | BCAR3 activity raises FHOD3's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.71× lower at baseline in the lines without BCAR3 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[MCOLN2]] | B | MCOLN2 activity raises FHOD3's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.38× lower at baseline in the lines without MCOLN2 | 0.088 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[AMOTL1]] | C | AMOTL1 activity raises FHOD3's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 3.74× lower at baseline in the lines without AMOTL1 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN; co-absent with the target |
| [[RGS17]] | C | RGS17 activity raises FHOD3's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 3.66× lower at baseline in the lines without RGS17 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1; co-absent with the target |
| [[FAM124A]] | C | FAM124A activity raises FHOD3's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 4.14× lower at baseline in the lines without FAM124A | 0.049 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1; co-absent with the target |
| [[SPRY4-AS1]] | C | SPRY4-AS1 activity raises FHOD3's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 4.81× lower at baseline in the lines without SPRY4-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROR1]] | B | FHOD3 activity raises ROR1's level | lines that do not express FHOD3 (14) vs lines expressing it (36) | 2.42× lower at baseline in the lines without FHOD3 | 0.067 | ⚠ within organs, on part of the lines; also absent: GJC1, ENSG00000267405, MAMLD1 |
| cells under [[Cobimetinib (drug)]] 5 µM | B | FHOD3 activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express FHOD3 (14) vs lines expressing it (34) | the lines without FHOD3: 1.19× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: GJC1, ENSG00000267405, MAMLD1 |
| cells under [[Cobimetinib (drug)]] 0.5 µM | B | FHOD3 activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express FHOD3 (14) vs lines expressing it (34) | the lines without FHOD3: 1.22× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: GJC1, ENSG00000267405, MAMLD1 |
| [[ATP13A3]] | B | FHOD3 activity raises ATP13A3's level | lines that do not express FHOD3 (14) vs lines expressing it (36) | 1.63× lower at baseline in the lines without FHOD3 | 0.082 | ⚠ within organs, on part of the lines; also absent: GJC1, ENSG00000267405, MAMLD1 |
| [[MTCP1]] | B | FHOD3 activity lowers MTCP1's level | lines that do not express FHOD3 (14) vs lines expressing it (36) | 1.39× higher at baseline in the lines without FHOD3 | 0.096 | ⚠ within organs, on part of the lines; also absent: GJC1, ENSG00000267405, MAMLD1 |
| [[AMOTL1]] | C | FHOD3 activity raises AMOTL1's level | lines that do not express FHOD3 (14) vs lines expressing it (36) | 4.30× lower at baseline in the lines without FHOD3 | 0.013 | ⚠ within organs, on part of the lines; also absent: GJC1, ENSG00000267405, MAMLD1; co-absent with the target |
| [[FAM124A]] | C | FHOD3 activity raises FAM124A's level | lines that do not express FHOD3 (14) vs lines expressing it (36) | 2.37× lower at baseline in the lines without FHOD3 | 0.037 | ⚠ within organs, on part of the lines; also absent: GJC1, ENSG00000267405, MAMLD1; co-absent with the target |
| [[RGS17]] | C | FHOD3 activity raises RGS17's level | lines that do not express FHOD3 (14) vs lines expressing it (36) | 4.56× lower at baseline in the lines without FHOD3 | 0.078 | ⚠ within organs, on part of the lines; also absent: GJC1, ENSG00000267405, MAMLD1; co-absent with the target |

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.1, 8.9); signed map (1.7, 56.2). **Vector** length 113, 31.3% of its response variance represented; |z| ≥ 3 in 1,299 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | +6.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +6.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +4.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.7 | +4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.2 | +3.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.2 | -8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.7 | -15.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -13.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.8 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.7 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -9.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | formin homology 2 domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.2 — chr18:36,297,713-36,780,220 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FHOS2, KIAA1695, FLJ22297, FLJ22717 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Formins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2V2M9](https://www.uniprot.org/uniprotkb/Q2V2M9) (FH1/FH2 domain-containing protein 3):

> Actin-organizing protein that may cause stress fiber formation together with cell elongation (By similarity). Isoform 4 may play a role in actin filament polymerization in cardiomyocytes.

**Summary**, from NCBI Gene [80206](https://www.ncbi.nlm.nih.gov/gene/80206):

> The protein encoded by this gene is a member of the diaphanous-related formins (DRF), and contains multiple domains, including GBD (GTPase-binding domain), DID (diaphanous inhibitory domain), FH1 (formin homology 1), FH2 (formin homology 2), and DAD (diaphanous auto-regulatory domain) domains. This protein is thought to play a role in actin filament polymerization in cardiomyocytes. Mutations in this gene have been associated with dilated cardiomyopathy (DCM), characterized by dilation of the …

**Accessions** — [HGNC:26178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26178) · Entrez [80206](https://www.ncbi.nlm.nih.gov/gene/80206) · UniProt [Q2V2M9](https://www.uniprot.org/uniprotkb/Q2V2M9) · Ensembl [ENSG00000134775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134775)

## Data

Gene col 5603: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5603); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5603, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5603]; `tensor/DDL_lfc|DDL_z.npy` [5603]; `embed/gene_vectors.npy` [5603]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5603 or target_col == 5603). Every well: [[FHOD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FHOD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
