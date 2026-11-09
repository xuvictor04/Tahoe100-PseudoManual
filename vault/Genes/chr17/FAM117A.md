---
symbol: "FAM117A"
type: "gene"
col: 4255
ensembl_id: "ENSG00000121104"
name: "family with sequence similarity 117 member A"
location: "17q21.33"
module: 4
arm: "-"
pooled_cpm: 17.39
n_lines_expressing: 48
n_dd_up: 30
n_dd_down: 18
n_dd_up_clean: 25
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# FAM117A

*family with sequence similarity 117 member A* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.19× (z +32.3, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.667× (z -6.5, q 5e-08, down in 24 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Pralsetinib (drug)]] 5 µM: 0.601× (z -4.3, q 0.003, down in 14 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSRP1]] (+0.70, fdr 7e-06), [[TSC22D4]] (+0.70, fdr 2e-05), [[CCNG2]] (+0.69, fdr 2e-05); moves opposite to [[HERC2]] (-0.71, fdr 8e-06), [[DIS3L2]] (-0.71, fdr 7e-06), [[CHCHD6]] (-0.70, fdr 1e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4255.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.19×** | +32.3 | 0e+00 | 45/45 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.15×** | +32.1 | 0e+00 | 42/44 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **5.33×** | +26.7 | 0e+00 | 44/46 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.06×** | +25.9 | 0e+00 | 43/46 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.12×** | +18.1 | 0e+00 | 39/46 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +17.4 | 0e+00 | 37/44 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.60×** | +15.2 | 0e+00 | 40/46 (HEC-1-A, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +14.4 | 6e-45 | 32/44 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +11.8 | 2e-30 | 29/44 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +10.5 | 4e-24 | 37/46 (J82, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +9.5 | 7e-20 | 30/45 (J82, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +9.2 | 1e-18 | 29/46 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +9.1 | 3e-18 | 26/46 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +8.6 | 2e-16 | 28/46 (SW1417, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.17×** | +6.5 | 4e-09 | 26/45 (A498, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4255.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.667×** | -6.5 | 5e-08 | 24/46 (HT-29, CHP-212, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **0.757×** | -4.5 | 0.002 | 19/38 (RPMI-7951, HEC-1-A, …) | rises with dose | composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **0.601×** | -4.3 | 0.003 | 14/41 (J82, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.760×** | -4.2 | 0.003 | 11/26 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.634×** | -3.8 | 0.016 | 8/25 (SW1417, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.797×** | -3.6 | 0.027 | 8/45 (HS-578T, SW480, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.860× | -3.4 | 0.045 | 9/46 (KATO III, HT-29, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.668×** | -3.4 | 0.045 | 11/46 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.803×** | -3.3 | 0.045 | 11/46 (RPMI-7951, HEC-1-A, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.805×** | -3.3 | 0.045 | 14/45 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.806×** | -3.3 | 0.045 | 10/45 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **0.815×** | -3.3 | 0.049 | 15/44 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Rosiglitazone (drug)]] 5 µM |  | **0.814×** | -3.2 | 0.067 | 9/44 (SW 900, HCT15, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.871× | -3.1 | 0.070 | 14/46 (H4, HEC-1-A, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.755×** | -3.1 | 0.081 | 8/44 (MIA PaCa-2, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.875× | -3.0 | 0.081 | 8/46 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.824×** | -3.0 | 0.081 | 6/46 (Hs 766T, SW48, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.701×** | -3.0 | 0.081 | 10/43 (A-172, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.831×** | -3.0 | 0.081 | 10/45 (HT-29, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4255. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 25.3 | 8 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.214× (z -12.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 18.4 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.50× (z +17.1) | — |
| [[J82 (line)]] | alt | 13.0 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.62× (z +17.3) | — |
| [[NCI-H460 (line)]] | wt | 6.29 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +17.6) | — |
| [[A498 (line)]] | wt | 19.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.61× (z +23.2) | — |
| [[BT-474 (line)]] | alt | 36.4 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +20.3) | — |
| [[HEC-1-A (line)]] | alt | 38.9 | 6 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +17.1) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[HS-578T (line)]] | alt | 12.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +15.2) | — |
| [[SW480 (line)]] | alt | 23.6 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +17.1) | — |
| [[C32 (line)]] | wt | 16.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +13.4) | — |
| [[LoVo (line)]] | wt | 13.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 8.61 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +18.2) | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[Panc 03.27 (line)]] | alt | 28.1 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[SNU-423 (line)]] | alt | 27.5 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -13.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 28.7 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.42× (z +16.1) | [[Lonafarnib (drug)]] 5 µM 0.0558× (z -11.4) ⚠ toxic |
| [[A549 (line)]] | wt | 6.06 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 26.4× (z +14.4) | [[Monocrotaline (drug)]] 0.05 µM 0.101× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 17.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -8.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +15.9) | — |
| [[A-172 (line)]] | wt | 19.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +15.2) | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[SW 900 (line)]] | alt | 24.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +10.5) | [[Oxaprozin (drug)]] 0.5 µM 0.132× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 17.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.10× (z +11.7) | — |
| [[RPMI-7951 (line)]] | alt | 22.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0693× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[A-427 (line)]] | wt | 18.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.65× (z +12.5) | — |
| [[CHP-212 (line)]] | wt | 36.9 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0955× (z -8.9) |
| [[COLO 205 (line)]] | alt | 16.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +8.8) | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0819× (z -11.2) |
| [[H4 (line)]] | wt | 18.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +9.0) | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.105× (z -9.0) |
| [[Hs 766T (line)]] | wt | 6.78 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.49× (z +10.6) | — |
| [[LS 180 (line)]] | wt | 18.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +11.8) | — |
| [[NCI-H23 (line)]] | alt | 19.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +12.6) | — |
| [[HT-29 (line)]] | alt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +11.0) | — |
| [[KATO III (line)]] | alt | 7.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +9.3) | — |
| [[SW48 (line)]] | wt | 15.9 | 0 | 1 | — | [[Verteporfin (drug)]] 0.05 µM 0.0794× (z -9.5) |
| [[AN3 CA (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4255), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSRP1]] | +0.70 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TSC22D4]] | +0.70 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[CCNG2]] | +0.69 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[CD27-AS1]] | +0.65 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[SMIM4]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[LASP1]] | +0.63 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[CDK19]] | +0.62 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[STX17-DT]] | +0.62 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[BET1]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ATOSA]] | +0.61 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[OSER1-DT]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ERO1B]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2]] | -0.71 | -0.68 / -0.58 | both halves | 8e-06 |  |
| [[DIS3L2]] | -0.71 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[CHCHD6]] | -0.70 | -0.75 / -0.57 | both halves | 1e-05 |  |
| [[COA1]] | -0.69 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[EIF2B3]] | -0.68 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[NAA15]] | -0.66 | -0.57 / -0.61 | both halves | 8e-06 |  |
| [[HERC2P9]] | -0.66 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[XRN2]] | -0.65 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[VWA8]] | -0.65 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[POLR3B]] | -0.64 | -0.63 / -0.46 | both halves | 2e-05 |  |
| [[TCOF1]] | -0.64 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.63 | -0.49 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FAM117A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[VASN]] | B | VASN activity raises FAM117A's level | lines that do not express VASN (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without VASN | 0.056 | ⚠ within organs, on part of the lines; also absent: PAQR7, DBN1, C5AR1; maybe low, not absent |
| [[LAMTOR3]] | C | LAMTOR3's natural level weakens FAM117A's drug response | LAMTOR3's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.01; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.5, -39.9); signed map (-11.4, 9.2). **Vector** length 75.7, 15.9% of its response variance represented; |z| ≥ 3 in 1,237 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +15.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +32.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +10.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +14.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.7 | +5.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +0.9 |
|  | [[Posaconazole (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -2.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 117 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:49,710,332-49,789,180 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q9C073](https://www.uniprot.org/uniprotkb/Q9C073) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:24179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24179) · Entrez [81558](https://www.ncbi.nlm.nih.gov/gene/81558) · UniProt [Q9C073](https://www.uniprot.org/uniprotkb/Q9C073) · Ensembl [ENSG00000121104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121104)

## Data

Gene col 4255: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4255); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4255, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4255]; `tensor/DDL_lfc|DDL_z.npy` [4255]; `embed/gene_vectors.npy` [4255]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4255 or target_col == 4255). Every well: [[FAM117A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM117A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
