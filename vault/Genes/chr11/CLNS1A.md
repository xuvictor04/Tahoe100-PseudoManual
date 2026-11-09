---
symbol: "CLNS1A"
type: "gene"
col: 1071
ensembl_id: "ENSG00000074201"
name: "chloride nucleotide-sensitive channel 1A"
location: "11q14.1"
module: 20
arm: "+"
pooled_cpm: 89.25
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# CLNS1A

*chloride nucleotide-sensitive channel 1A* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.94× (z +20.7, q 0e+00, up in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +15.4, q 0e+00, up in 32 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.639× (z -13.5, q 1e-38, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBFD1]] (+0.62, fdr 1e-05), [[THOC5]] (+0.58, fdr 1e-05), [[CNBP]] (+0.58, fdr 1e-05); moves opposite to [[DPF1]] (-0.55, fdr 2e-05), [[LRRC8E]] (-0.51, fdr 1e-04), [[ARL4D]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1071.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +20.7 | 0e+00 | 43/49 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +18.5 | 0e+00 | 33/44 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +15.4 | 0e+00 | 32/49 (NCI-H1792, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +13.0 | 1e-36 | 35/45 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +9.7 | 3e-20 | 36/47 (MIA PaCa-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +9.7 | 5e-20 | 30/48 (NCI-H23, SW 900, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +7.7 | 2e-12 | 33/50 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +6.9 | 5e-10 | 0/50 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +6.8 | 9e-10 | 25/48 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.24×** | +6.6 | 2e-09 | 26/48 (A-172, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +6.1 | 5e-08 | 17/48 (CFPAC-1, BT-474, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.18× | +5.2 | 1e-05 | 22/48 (A-172, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.15× | +4.5 | 3e-04 | 19/48 (A-172, hTERT-HPNE, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.10× | +4.3 | 8e-04 | 15/48 (NCI-H1573, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.15× | +4.2 | 9e-04 | 17/48 (A-172, NCI-H2030, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 5 µM |  | 1.14× | +4.0 | 0.002 | 12/47 (A-427, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.12× | +3.4 | 0.017 | 12/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.11× | +3.3 | 0.031 | 5/48 (NCI-H23, SNU-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 5 µM |  | 1.07× | +3.0 | 0.064 | 0/49 | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 1.11× | +3.0 | 0.064 | 8/49 (SNU-423, SW1417, …) | top dose only |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.064 | 4/48 (LOX-IMVI, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[Vismodegib (drug)]] 0.5 µM |  | 1.10× | +3.0 | 0.070 | 7/48 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1071.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.639×** | -13.5 | 1e-38 | 37/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.757×** | -12.3 | 2e-32 | 28/48 (PANC-1, A-427, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.677×** | -12.2 | 6e-32 | 42/48 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.624×** | -7.7 | 2e-12 | 28/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.803×** | -6.9 | 8e-10 | 26/48 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.737×** | -6.8 | 9e-10 | 33/48 (PANC-1, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.661×** | -6.8 | 1e-09 | 29/48 (Hs 766T, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.664×** | -6.7 | 2e-09 | 28/48 (PANC-1, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.756×** | -6.3 | 2e-08 | 28/49 (PANC-1, NCI-H23, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.765×** | -6.0 | 1e-07 | 29/48 (PANC-1, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.829×** | -5.9 | 2e-07 | 20/48 (PANC-1, AsPC-1, …) | rises with dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.718×** | -5.4 | 3e-06 | 25/48 (PANC-1, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.836× | -5.3 | 5e-06 | 20/48 (LoVo, RKO, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.739×** | -4.9 | 3e-05 | 19/48 (A498, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.850× | -4.8 | 5e-05 | 16/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.770×** | -4.3 | 7e-04 | 20/48 (Panc 03.27, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 5 µM |  | 0.895× | -3.4 | 0.024 | 7/48 (HEC-1-A, Panc 03.27, …) | rises with dose | position effect removed |
| [[Posaconazole (drug)]] 5 µM |  | 0.908× | -2.9 | 0.095 | 4/48 (MIA PaCa-2, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[PF-06260933 (drug)]] 5 µM |  | 0.837× | -2.9 | 0.095 | 8/48 (A-172, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1071. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 113 | 1 (1 ⚠) | 8 (7 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.59× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -24.9) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.399× (z -16.5) |
| [[MIA PaCa-2 (line)]] | alt | 110 | 4 (3 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -12.8) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.521× (z -9.4) |
| [[A-172 (line)]] | wt | 82.9 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.07× (z +9.9) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 63.9 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.65× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -18.3) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.434× (z -9.1) |
| [[HOP62 (line)]] | alt | 61.3 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +11.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.502× (z -8.8) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 64.2 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.628× (z -9.4) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SW480 (line)]] | alt | 110 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.12× (z +14.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.659× (z -11.4) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.578× (z -10.2) |
| [[A498 (line)]] | wt | 54.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -14.2) ⚠ cell-cycle shift, explains ~22% of this change |
| [[HEC-1-A (line)]] | alt | 148 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -11.7) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.479× (z -9.5) |
| [[HT-29 (line)]] | alt | 85.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +10.4) | — |
| [[LoVo (line)]] | wt | 106 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.74× (z +15.8) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.586× (z -8.7) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 62.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 53.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +17.4) | — |
| [[NCI-H2030 (line)]] | alt | 72.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +11.1) | — |
| [[A-427 (line)]] | wt | 181 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -21.3) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.547× (z -8.5) |
| [[A549 (line)]] | wt | 87.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +13.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 188 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +13.7) | — |
| [[NCI-H2347 (line)]] | alt | 69.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 117 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +9.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.436× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 62.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.397× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~11% of this change |
| [[C32 (line)]] | wt | 98.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -12.1) ⚠ cell-cycle shift, explains ~22% of this change |
| [[CFPAC-1 (line)]] | alt | 61.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +13.7) | — |
| [[HCT15 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.1) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[Hs 766T (line)]] | wt | 69.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 79.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 83.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -13.5) ⚠ cell-cycle shift, explains ~22% of this change |
| [[J82 (line)]] | alt | 98.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +9.3) | — |
| [[KATO III (line)]] | alt | 95.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 93.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +10.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 94.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 74.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.567× (z -9.0) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SNU-1 (line)]] | wt | 84.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 48.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.629× (z -9.3) ⚠ cell-cycle shift, explains ~22% of this change |
| [[AN3 CA (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 100 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 88.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1071), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBFD1]] | +0.62 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[THOC5]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CNBP]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[NIT2]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[DUXAP8]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[MRE11]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[EEF1A1P5]] | +0.55 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ZBTB44]] | +0.55 | +0.32 / +0.60 | both halves | 1e-04 |  |
| [[ZNF37BP]] | +0.55 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[EEF1A1]] | +0.55 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[MSL3]] | +0.54 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[NAF1]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPF1]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[LRRC8E]] | -0.51 | -0.32 / -0.46 | both halves | 1e-04 | STRING 405 |
| [[ARL4D]] | -0.50 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[NAT14]] | -0.50 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[VPS18]] | -0.50 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[MIDN]] | -0.50 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[ZNF503]] | -0.50 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[NFKBIE]] | -0.50 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CEP19]] | -0.48 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[CCDC88A]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[JUND]] | -0.48 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[BIK]] | -0.48 | -0.44 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CLNS1A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.481). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-26.0, -29.5); signed map (-22.4, -48.2). **Vector** length 107, 27.4% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.7 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.3 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +13.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +7.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +3.3 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.3 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.1 | -13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -7.2 | -12.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.9 | -12.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.9 | -6.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.7 | -5.4 |
|  | [[EX229 (drug)]] 5 µM |  | -4.5 | -4.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -4.2 | -6.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.1 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | chloride nucleotide-sensitive channel 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:77,514,936-77,637,794 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ICln; previously CLCI |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 3 pathways, smallest: Metabolism of non-coding RNA; snRNP Assembly; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P54105](https://www.uniprot.org/uniprotkb/P54105) (Methylosome subunit pICln):

> Involved in both the assembly of spliceosomal snRNPs and the methylation of Sm proteins. Chaperone that regulates the assembly of spliceosomal U1, U2, U4 and U5 small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome, and thereby plays an important role in the splicing of cellular pre-mRNAs. Most spliceosomal snRNPs contain a common set of Sm proteins SNRPB, SNRPD1, SNRPD2, SNRPD3, SNRPE, SNRPF and SNRPG that assemble in a heptameric protein ring on the Sm site of the …

**Summary**, from NCBI Gene [1207](https://www.ncbi.nlm.nih.gov/gene/1207):

> This gene encodes a protein that functions in multiple regulatory pathways. The encoded protein complexes with numerous cytosolic proteins and performs diverse functions including regulation of small nuclear ribonucleoprotein biosynthesis, platelet activation and cytoskeletal organization. The protein is also found associated with the plasma membrane where it functions as a chloride current regulator. Pseudogenes of this gene are found on chromosomes 1, 4 and 6. Several transcript variants …

**Accessions** — [HGNC:2080](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2080) · Entrez [1207](https://www.ncbi.nlm.nih.gov/gene/1207) · UniProt [P54105](https://www.uniprot.org/uniprotkb/P54105) · Ensembl [ENSG00000074201](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074201)

## Data

Gene col 1071: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1071); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1071, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1071]; `tensor/DDL_lfc|DDL_z.npy` [1071]; `embed/gene_vectors.npy` [1071]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1071 or target_col == 1071). Every well: [[CLNS1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLNS1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
