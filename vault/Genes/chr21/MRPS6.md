---
symbol: "MRPS6"
type: "gene"
col: 14380
ensembl_id: "ENSG00000243927"
name: "mitochondrial ribosomal protein S6"
location: "21q22.11"
module: 1
arm: "-"
pooled_cpm: 143.48
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 32
n_dd_up_clean: 15
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MRPS6

*mitochondrial ribosomal protein S6* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.68× (z +14.5, q 4e-45, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.227× (z -15.3, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC5A3]] (+0.90, fdr 7e-06, ⚠ same locus), [[LINC00310]] (+0.84, fdr 7e-06, ⚠ same locus), [[TESK2]] (+0.59, fdr 1e-05), [[NPTX1]] (+0.58, fdr 1e-05), [[ADCY10]] (+0.56, fdr 3e-05); moves opposite to [[SCAP]] (-0.62, fdr 7e-06), [[FKTN]] (-0.59, fdr 1e-05), [[PPP5C]] (-0.59, fdr 3e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14380.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +14.5 | 4e-45 | 34/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +14.3 | 7e-44 | 41/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +14.3 | 7e-44 | 41/49 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +8.0 | 3e-13 | 27/47 (BT-474, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +6.1 | 2e-07 | 30/47 (LoVo, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +5.2 | 2e-05 | 25/47 (LoVo, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.27×** | +4.8 | 2e-04 | 26/47 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.25×** | +4.4 | 7e-04 | 21/47 (COLO 205, SW1417, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.004 | 21/48 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[NG25 (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.006 | 19/46 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.008 | 21/47 (LoVo, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Gefitinib (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.010 | 19/47 (NCI-H460, SNU-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.20×** | +3.7 | 0.010 | 19/47 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.010 | 19/46 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.028 | 14/47 (A-172, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14380.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.227×** | -15.3 | 0e+00 | 47/48 (CFPAC-1, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.614×** | -9.6 | 2e-19 | 32/47 (C32, A-172, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.396×** | -9.6 | 2e-19 | 38/47 (C32, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.639×** | -8.8 | 1e-16 | 33/47 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.635×** | -8.6 | 7e-16 | 32/46 (C32, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.658×** | -8.3 | 1e-14 | 39/47 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.672×** | -7.9 | 3e-13 | 31/47 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.685×** | -7.5 | 6e-12 | 27/47 (HOP62, A498, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.694×** | -6.9 | 3e-10 | 26/47 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.722×** | -6.4 | 7e-09 | 31/47 (HS-578T, A-172, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.741×** | -5.9 | 2e-07 | 28/47 (C32, CFPAC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.748×** | -5.7 | 5e-07 | 26/47 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.757×** | -5.5 | 2e-06 | 25/47 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.588×** | -5.5 | 2e-06 | 17/36 (C32, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.745×** | -5.4 | 3e-06 | 26/45 (NCI-H1792, NCI-H23, …) | all doses, flat | composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.763×** | -5.3 | 3e-06 | 22/47 (HS-578T, NCI-H1792, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.756×** | -5.3 | 4e-06 | 25/48 (HS-578T, A498, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.765×** | -5.3 | 4e-06 | 25/47 (A498, HS-578T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.768×** | -5.2 | 6e-06 | 23/47 (HOP62, HS-578T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14380. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 317 | 0 | 39 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.220× (z -15.8) |
| [[HOP62 (line)]] | alt | 250 | 0 | 26 (8 ⚠) | — | [[Budesonide (drug)]] 0.05 µM 0.253× (z -15.3) |
| [[NCI-H2347 (line)]] | alt | 200 | 0 | 26 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.276× (z -11.7) ⚠ toxic · without an alert: [[Dexamethasone (drug)]] 0.05 µM 0.295× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 286 | 0 | 25 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.270× (z -13.2) |
| [[A-172 (line)]] | wt | 255 | 0 | 24 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -20.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.250× (z -16.1) |
| [[A498 (line)]] | wt | 185 | 3 (1 ⚠) | 18 | [[Selinexor (drug)]] 5 µM 2.20× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +10.9) | [[Triamcinolone (drug)]] 0.5 µM 0.238× (z -15.5) |
| [[C32 (line)]] | wt | 335 | 0 | 16 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.107× (z -22.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.197× (z -17.1) |
| [[NCI-H1573 (line)]] | alt | 164 | 0 | 15 (2 ⚠) | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.247× (z -11.9) |
| [[SW 900 (line)]] | alt | 342 | 0 | 14 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.189× (z -12.8) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.0797× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 355 | 1 (1 ⚠) | 11 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.99× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Belinostat (drug)]] 5 µM 0.281× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 318 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.402× (z -9.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.410× (z -9.7) |
| [[BT-474 (line)]] | alt | 42.7 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.90× (z +16.4) | — |
| [[hTERT-HPNE (line)]] | wt | 210 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -12.1) |
| [[LoVo (line)]] | wt | 81.2 | 8 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +15.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 76.0 | 7 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.09× (z +20.7) | — |
| [[HEC-1-A (line)]] | alt | 68.1 | 4 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +14.8) | [[TAK-901 (drug)]] 5 µM 0.215× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 43.8 | 5 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.43× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 308 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.170× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 40.3 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +19.6) | — |
| [[Panc 03.27 (line)]] | alt | 70.8 | 4 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +16.2) | [[TAK-901 (drug)]] 5 µM 0.160× (z -9.8) |
| [[SNU-423 (line)]] | alt | 89.3 | 1 | 4 | [[Auranofin (drug)]] 5 µM 3.56× (z +11.0) | [[Clobetasol propionate (drug)]] 5 µM 0.340× (z -9.2) |
| [[C-33 A (line)]] | alt | 68.8 | 4 (1 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +11.3) | — |
| [[COLO 205 (line)]] | alt | 94.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.42× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 53.7 | 4 | 0 | [[Auranofin (drug)]] 5 µM 5.39× (z +15.6) | — |
| [[PANC-1 (line)]] | alt | 136 | 0 | 4 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.199× (z -10.7) |
| [[A-427 (line)]] | wt | 51.3 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.58× (z +15.3) | — |
| [[H4 (line)]] | wt | 82.1 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.00× (z +13.9) | — |
| [[J82 (line)]] | alt | 43.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +13.1) | — |
| [[LOX-IMVI (line)]] | wt | 78.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +17.1) | — |
| [[LS 180 (line)]] | wt | 142 | 1 | 2 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +8.9) | [[TAK-901 (drug)]] 5 µM 0.122× (z -10.4) |
| [[RKO (line)]] | wt | 64.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +17.6) | — |
| [[SK-MEL-2 (line)]] | alt | 64.9 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.07× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SNU-1 (line)]] | wt | 63.9 | 2 | 1 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +11.5) | [[PH-797804 (drug)]] 5 µM 0.0521× (z -11.4) |
| [[A549 (line)]] | wt | 36.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 94.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.6) | [[TAK-901 (drug)]] 5 µM 0.200× (z -8.5) |
| [[SHP-77 (line)]] | alt | 162 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 166 | 0 | 2 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0634× (z -10.8) |
| [[AN3 CA (line)]] | alt | 83.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[CHP-212 (line)]] | wt | 82.8 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0284× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 52.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +16.5) | — |
| [[RPMI-7951 (line)]] | alt | 49.0 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 97.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.0) | — |
| [[SW48 (line)]] | wt | 128 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.273× (z -9.2) |
| [[SW480 (line)]] | alt | 219 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.271× (z -12.3) ⚠ toxic |
| [[HCT15 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14380), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*32 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC5A3]] | +0.90 | +0.93 / +0.87 | both halves | 7e-06 | STRING 695; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LINC00310]] | +0.84 | +0.79 / +0.87 | both halves | 7e-06 | ⚠ same locus (14.7 kb, same strand: neighbours can correlate without regulation) |
| [[TESK2]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[NPTX1]] | +0.58 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[ADCY10]] | +0.56 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[GDNF-AS1]] | +0.55 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[IQCJ]] | +0.54 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[ACVR1C]] | +0.54 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[SYNJ2]] | +0.54 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[CXCR4]] | +0.51 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[CD27-AS1]] | +0.50 | +0.31 / +0.45 | both halves | 2e-04 |  |
| [[TPBG]] | +0.50 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[SMIM4]] | +0.50 | +0.44 / +0.39 | both halves | 5e-05 |  |
| [[PTHLH]] | +0.50 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*68 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAP]] | -0.62 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[FKTN]] | -0.59 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[PPP5C]] | -0.59 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[MAOA]] | -0.59 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[MRPL3]] | -0.58 | -0.52 / -0.57 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 998 |
| [[ARMC8]] | -0.57 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[RAD51D]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[AGK]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[DLAT]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[RIOK1]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[LTBR]] | -0.54 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[MRPL42]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 984 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers MRPS6's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity lowers MRPS6's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (44.2, -10.7); signed map (9.3, 18.3). **Vector** length 148, 48.3% of its response variance represented; |z| ≥ 3 in 1,913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +12.3 | +14.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +12.0 | +14.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +14.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.7 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | +3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.7 | +1.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +2.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -10.6 | -15.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -7.5 | -5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.4 | -9.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -6.8 | -5.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -6.7 | -7.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -6.6 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:34,073,224-34,143,034 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-S6, RPMS6, bS6m; previously C21orf101 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [P82932](https://www.uniprot.org/uniprotkb/P82932) carries no function annotation.

**Summary**, from NCBI Gene [64968](https://www.ncbi.nlm.nih.gov/gene/64968):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14051](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14051) · Entrez [64968](https://www.ncbi.nlm.nih.gov/gene/64968) · UniProt [P82932](https://www.uniprot.org/uniprotkb/P82932) · Ensembl [ENSG00000243927](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243927)

## Data

Gene col 14380: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14380); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14380, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14380]; `tensor/DDL_lfc|DDL_z.npy` [14380]; `embed/gene_vectors.npy` [14380]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14380 or target_col == 14380). Every well: [[MRPS6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
