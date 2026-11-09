---
symbol: "CDA"
type: "gene"
col: 8195
ensembl_id: "ENSG00000158825"
name: "cytidine deaminase"
location: "1p36.12"
module: 137
arm: "-"
pooled_cpm: 27.79
n_lines_expressing: 34
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 11
direction_downstream: 23
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# CDA

*cytidine deaminase* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.35× (z +18.3, q 0e+00, up in 24 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.68× (z +6.3, q 5e-08, up in 27 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.300× (z -9.8, q 6e-20, down in 28 of 31 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPMT]] (+0.66, fdr 1e-05), [[LMTK3]] (+0.63, fdr 2e-05), [[PRKCI]] (+0.62, fdr 2e-05); moves opposite to [[ARID1B]] (-0.59, fdr 5e-05), [[ARID1A]] (-0.59, fdr 4e-05), [[ZNF689]] (-0.59, fdr 3e-05).
> It sits in the **-** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SULT2B1]] → it (grade B ⚠); 23 go from it, the strongest it → [[ATR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8195.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.35×** | +18.3 | 0e+00 | 24/25 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.07×** | +16.6 | 0e+00 | 29/29 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.39×** | +11.6 | 5e-29 | 23/26 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +6.3 | 5e-08 | 27/32 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +5.2 | 2e-05 | 24/32 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.76×** | +4.8 | 2e-04 | 12/31 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +4.1 | 0.004 | 13/32 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.010 | 12/32 (HepG2/C3A, LS 180, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.25×** | +3.6 | 0.019 | 9/19 (HOP62, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.055 | 14/31 (SW480, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.1 | 0.088 | 14/31 (CFPAC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8195.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.300×** | -9.8 | 6e-20 | 28/31 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.425×** | -7.0 | 9e-10 | 25/32 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.447×** | -6.8 | 2e-09 | 23/32 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.578×** | -6.6 | 8e-09 | 25/32 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.684×** | -4.5 | 7e-04 | 21/32 (CFPAC-1, A549, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.603×** | -4.0 | 0.005 | 18/32 (SNU-423, A498, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.638×** | -3.8 | 0.012 | 16/32 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.639×** | -3.6 | 0.020 | 17/32 (CFPAC-1, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.644×** | -3.6 | 0.022 | 18/32 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.661×** | -3.5 | 0.026 | 14/32 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.673×** | -3.3 | 0.043 | 10/31 (CFPAC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.679×** | -3.3 | 0.051 | 17/31 (CFPAC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -3.2 | 0.056 | 18/30 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.690×** | -3.1 | 0.070 | 11/32 (HepG2/C3A, A549, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.696×** | -3.1 | 0.084 | 15/31 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 87.3 | 2 (2 ⚠) | 9 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.06× (z +11.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -18.5) |
| [[LS 180 (line)]] | wt | 76.2 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -21.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -17.3) |
| [[LoVo (line)]] | wt | 39.0 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 20.1× (z +19.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 177 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.07× (z +12.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 33.4 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.76× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -12.1) |
| [[A549 (line)]] | wt | 41.3 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 8.14× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -12.6) |
| [[HT-29 (line)]] | alt | 42.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0781× (z -22.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -18.0) |
| [[SW480 (line)]] | alt | 29.6 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 12.4× (z +16.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -11.5) |
| [[HOP62 (line)]] | alt | 42.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 32.9× (z +19.5) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 52.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 9.83× (z +11.2) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -10.0) |
| [[COLO 205 (line)]] | alt | 33.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 92.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -15.9) |
| [[HS-578T (line)]] | alt | 11.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 43.1× (z +11.0) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0503× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 21.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 9.91× (z +12.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -8.6) |
| [[A498 (line)]] | wt | 21.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.11× (z +9.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 37.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 17.1× (z +11.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 11.1 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 6.87× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 30.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.89× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 62.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.01× (z +11.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 12.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 51.7× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 35.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.2× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 7.67 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.4× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 17.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -8.5) |
| [[SW 900 (line)]] | alt | 11.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 21.5× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.25 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.80 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.98 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.30 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPMT]] | +0.66 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[LMTK3]] | +0.63 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[PRKCI]] | +0.62 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[HDAC11]] | +0.62 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[SGSM1]] | +0.61 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[FA2H]] | +0.59 | +0.73 / +0.35 | both halves | 1e-04 |  |
| [[MBOAT2]] | +0.58 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[FCHO1]] | +0.58 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[RGS9]] | +0.58 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[RAP1GAP]] | +0.57 | +0.43 / +0.57 | both halves | 3e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[SULT2B1]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[RCAN3]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID1B]] | -0.59 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[ARID1A]] | -0.59 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ZNF689]] | -0.59 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[ASXL2]] | -0.58 | -0.60 / -0.37 | both halves | 7e-05 |  |
| [[UBTF]] | -0.58 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[ATXN7]] | -0.56 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[CREBBP]] | -0.55 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[CASD1]] | -0.55 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[ENDOG]] | -0.54 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZNF629]] | -0.54 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[UBE3B]] | -0.54 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[TCF12]] | -0.53 | -0.57 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SULT2B1]] | B | SULT2B1 activity raises CDA's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.68× lower at baseline in the lines without SULT2B1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[NGEF]] | B | NGEF activity raises CDA's level | lines that do not express NGEF (12) vs lines expressing it (38) | 3.77× lower at baseline in the lines without NGEF | 0.005 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB |
| [[FA2H]] | B | FA2H activity raises CDA's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.80× lower at baseline in the lines without FA2H | 0.005 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[FUT2]] | B | FUT2 activity raises CDA's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 3.72× lower at baseline in the lines without FUT2 | 0.007 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises CDA's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PKP1]] | B | PKP1 activity raises CDA's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.72× lower at baseline in the lines without PKP1 | 0.028 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[SEMA3B]] | B | SEMA3B activity raises CDA's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.20× lower at baseline in the lines without SEMA3B | 0.045 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[LYPD3]] | B | LYPD3 activity raises CDA's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 2.05× lower at baseline in the lines without LYPD3 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[KRT17]] | B | KRT17 activity raises CDA's level | lines that do not express KRT17 (37) vs lines expressing it (13) | 2.09× lower at baseline in the lines without KRT17 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC5AC, FGFR2 |
| [[LMTK3]] | B | LMTK3 activity raises CDA's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 2.14× lower at baseline in the lines without LMTK3 | 0.093 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[KRT16]] | C | KRT16 activity raises CDA's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 2.72× lower at baseline in the lines without KRT16 | 0.004 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 22, C 1. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATR]] | B | CDA activity strengthens ATR's drug response | lines that do not express CDA (16) vs lines expressing it (34) | the lines without CDA respond 0.61× as strongly (z diff +1.87); strongest at Belinostat 5 µM: 1.42x vs 2.14x (z diff +3.1) | 0.004 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG; artifact flags |
| [[TOR1A]] | B | CDA activity lowers TOR1A's level | lines that do not express CDA (16) vs lines expressing it (34) | 1.28× higher at baseline in the lines without CDA | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[FA2H]] | B | CDA activity raises FA2H's level | lines that do not express CDA (16) vs lines expressing it (34) | 4.01× lower at baseline in the lines without CDA | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[ZNF689]] | B | CDA activity lowers ZNF689's level | lines that do not express CDA (16) vs lines expressing it (34) | 1.47× higher at baseline in the lines without CDA | 0.015 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[FUT2]] | B | CDA activity raises FUT2's level | lines that do not express CDA (16) vs lines expressing it (34) | 2.12× lower at baseline in the lines without CDA | 0.020 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[E2F3]] | B | CDA activity lowers E2F3's level | lines that do not express CDA (16) vs lines expressing it (34) | 1.48× higher at baseline in the lines without CDA | 0.020 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[SULT2B1]] | B | CDA activity raises SULT2B1's level | lines that do not express CDA (16) vs lines expressing it (34) | 2.55× lower at baseline in the lines without CDA | 0.023 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[FHIP1A]] | B | CDA activity raises FHIP1A's level | lines that do not express CDA (16) vs lines expressing it (34) | 2.66× lower at baseline in the lines without CDA | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[NGEF]] | B | CDA activity raises NGEF's level | lines that do not express CDA (16) vs lines expressing it (34) | 2.41× lower at baseline in the lines without CDA | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[F11R]] | B | CDA activity raises F11R's level | lines that do not express CDA (16) vs lines expressing it (34) | 2.96× lower at baseline in the lines without CDA | 0.032 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[GIPR]] | B | CDA activity raises GIPR's level | lines that do not express CDA (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without CDA | 0.037 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[CRYBG2]] | B | CDA activity raises CRYBG2's level | lines that do not express CDA (16) vs lines expressing it (34) | 2.85× lower at baseline in the lines without CDA | 0.037 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **-** arm (projection on the module's main direction -0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (11.1, 2.3); signed map (-19.3, 28.6). **Vector** length 103, 31.1% of its response variance represented; |z| ≥ 3 in 754 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.8 | +16.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.1 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.0 | +18.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +3.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.2 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -3.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | cytidine deaminase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:20,589,086-20,618,903 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDD |
| Hallmark sets | DNA_REPAIR, XENOBIOTIC_METABOLISM, COMPLEMENT |
| Reactome | 5 pathways, smallest: Pyrimidine salvage; Nucleotide salvage; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P32320](https://www.uniprot.org/uniprotkb/P32320) (Cytidine deaminase):

> This enzyme scavenges exogenous and endogenous cytidine and 2'-deoxycytidine for UMP synthesis.

**Summary**, from NCBI Gene [978](https://www.ncbi.nlm.nih.gov/gene/978):

> This gene encodes an enzyme involved in pyrimidine salvaging. The encoded protein forms a homotetramer that catalyzes the irreversible hydrolytic deamination of cytidine and deoxycytidine to uridine and deoxyuridine, respectively. It is one of several deaminases responsible for maintaining the cellular pyrimidine pool. Mutations in this gene are associated with decreased sensitivity to the cytosine nucleoside analogue cytosine arabinoside used in the treatment of certain childhood leukemias. …

**Accessions** — [HGNC:1712](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1712) · Entrez [978](https://www.ncbi.nlm.nih.gov/gene/978) · UniProt [P32320](https://www.uniprot.org/uniprotkb/P32320) · Ensembl [ENSG00000158825](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158825)

## Data

Gene col 8195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8195); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8195]; `tensor/DDL_lfc|DDL_z.npy` [8195]; `embed/gene_vectors.npy` [8195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8195 or target_col == 8195). Every well: [[CDA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
