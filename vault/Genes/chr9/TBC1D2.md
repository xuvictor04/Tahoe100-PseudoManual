---
symbol: "TBC1D2"
type: "gene"
col: 1744
ensembl_id: "ENSG00000095383"
name: "TBC1 domain family member 2"
location: "9q22.33"
module: 160
arm: "+"
pooled_cpm: 28.62
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# TBC1D2

*TBC1 domain family member 2* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.01× (z +12.0, q 2e-30, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.527× (z -15.5, q 0e+00, down in 33 of 43 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.450× (z -12.6, q 5e-34, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF18]] (+0.61, fdr 1e-05), [[ARPC5L]] (+0.58, fdr 1e-05), [[LUZP1]] (+0.58, fdr 1e-05); moves opposite to [[SUGT1P3]] (-0.57, fdr 2e-05), [[KPNA5]] (-0.55, fdr 1e-05), [[AMACR]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MICAL2]] → it (grade B ⚠); 4 go from it, the strongest it → [[TNFAIP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1744.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +12.0 | 2e-30 | 33/44 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.88×** | +10.8 | 7e-25 | 36/44 (A549, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +9.4 | 1e-18 | 25/41 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +8.5 | 2e-15 | 30/41 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +8.5 | 3e-15 | 26/44 (A549, KATO III, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +8.3 | 1e-14 | 25/44 (A549, A-427, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.87×** | +5.6 | 2e-06 | 15/44 (HOP62, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.24×** | +3.8 | 0.012 | 10/44 (LS 180, A498, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +3.3 | 0.057 | 8/44 (A-172, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.23×** | +3.3 | 0.057 | 16/43 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.075 | 10/42 (LoVo, A498, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.12 | 1/44 (J82) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1744.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.527×** | -15.5 | 0e+00 | 33/43 (LoVo, AsPC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.450×** | -12.6 | 5e-34 | 31/43 (Hs 766T, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.625×** | -11.4 | 1e-27 | 34/44 (J82, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.589×** | -9.1 | 2e-17 | 24/43 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.594×** | -8.9 | 5e-17 | 25/40 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.618×** | -8.2 | 2e-14 | 25/44 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.658×** | -6.6 | 3e-09 | 21/37 (LoVo, Hs 766T, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.682×** | -6.6 | 4e-09 | 20/43 (J82, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.684×** | -6.0 | 1e-07 | 20/29 (J82, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.707×** | -5.9 | 2e-07 | 20/42 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -5.4 | 4e-06 | 6/45 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.742×** | -5.1 | 2e-05 | 19/35 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.759×** | -4.7 | 1e-04 | 19/44 (LoVo, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.749×** | -4.6 | 2e-04 | 16/27 (Hs 766T, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | 0.843× | -4.1 | 0.002 | 17/44 (LoVo, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.817×** | -3.4 | 0.020 | 18/43 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.870× | -3.3 | 0.027 | 12/45 (LoVo, SNU-423, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.815×** | -3.2 | 0.038 | 12/41 (LoVo, KATO III, …) | rises with dose |  |
| [[Piroxicam (drug)]] 0.05 µM |  | 0.835× | -3.1 | 0.059 | 7/44 (AN3 CA, HepG2/C3A, …) | inconsistent across doses |  |
| [[Bexarotene (drug)]] 0.5 µM |  | 0.836× | -3.0 | 0.060 | 8/43 (J82, Hs 766T, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.824×** | -3.0 | 0.060 | 9/43 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.884× | -3.0 | 0.073 | 11/44 (HT-29, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1744. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 56.5 | 1 (1 ⚠) | 12 (6 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +8.6) ⚠ cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.0914× (z -29.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0816× (z -21.6) |
| [[Hs 766T (line)]] | wt | 138 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -17.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -14.0) |
| [[LS 180 (line)]] | wt | 45.7 | 3 (2 ⚠) | 4 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +14.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -10.5) |
| [[KATO III (line)]] | alt | 21.2 | 1 (1 ⚠) | 4 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.62× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0754× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -10.9) |
| [[J82 (line)]] | alt | 57.4 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.245× (z -17.4) |
| [[HEC-1-A (line)]] | alt | 40.5 | 3 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.18× (z +13.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +12.9) | — |
| [[HOP62 (line)]] | alt | 30.5 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.198× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 26.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -13.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.434× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 57.2 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.228× (z -10.0) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.427× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 16.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -15.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 40.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0778× (z -23.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.199× (z -9.9) |
| [[HCT15 (line)]] | alt | 49.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -14.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 38.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -11.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW480 (line)]] | alt | 22.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -18.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 64.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.325× (z -10.0) |
| [[A549 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -11.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 7.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.92× (z +12.0) | — |
| [[C-33 A (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0753× (z -10.3) |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[H4 (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0719× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 12.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.225× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 9.99 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.133× (z -10.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -15.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -10.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.102× (z -8.7) |
| [[SNU-423 (line)]] | alt | 19.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.239× (z -11.8) |
| [[A-172 (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.51 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.44 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.26 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.05 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1744), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF18]] | +0.61 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ARPC5L]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[LUZP1]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[FBXW7]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[MYO9B]] | +0.57 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[PTPN1]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[RABGEF1P1]] | +0.54 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[CDC42BPB]] | +0.54 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[ASAP2]] | +0.53 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[EHD4]] | +0.53 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[CCM2]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[TNFAIP1]] | +0.53 | +0.52 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGT1P3]] | -0.57 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[KPNA5]] | -0.55 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[AMACR]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CHIC1]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[PMPCB]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[C17orf75]] | -0.52 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[ZNF280D]] | -0.51 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[NDUFA5]] | -0.51 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[PGGT1B]] | -0.50 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[CCDC25]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ZDHHC17]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[STAG2]] | -0.50 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MICAL2]] | B | MICAL2 activity raises TBC1D2's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without MICAL2 | 0.017 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[GJB3]] | B | GJB3 activity raises TBC1D2's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 2.11× lower at baseline in the lines without GJB3 | 0.042 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[HDAC6]] | B | HDAC6 activity lowers TBC1D2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFAIP1]] | C | TBC1D2 activity raises TNFAIP1's level | lines that do not express TBC1D2 (4) vs lines expressing it (46) | 1.68× lower at baseline in the lines without TBC1D2 | 0.023 | ⚠ few lines (4 vs 46); across organs; also absent: ARHGAP27; maybe low, not absent |
| cells under [[Elimusertib hydrochloride (drug)]] 0.05 µM | C | TBC1D2 activity raises the cells' numbers under Elimusertib hydrochloride 0.05 µM (protects the cells) | lines that do not express TBC1D2 (4) vs lines expressing it (44) | the lines without TBC1D2: 0.73× the cells of the other lines | 0.060 | ⚠ few lines (4 vs 46); across organs; also absent: ARHGAP27; maybe low, not absent |
| cells under [[Cobimetinib (drug)]] 0.5 µM | C | TBC1D2 activity raises the cells' numbers under Cobimetinib 0.5 µM (protects the cells) | lines that do not express TBC1D2 (4) vs lines expressing it (44) | the lines without TBC1D2: 0.75× the cells of the other lines | 0.091 | ⚠ few lines (4 vs 46); across organs; also absent: ARHGAP27; maybe low, not absent |
| [[C16orf74]] | C | TBC1D2 activity raises C16orf74's level | lines that do not express TBC1D2 (4) vs lines expressing it (46) | 3.29× lower at baseline in the lines without TBC1D2 | 0.095 | ⚠ few lines (4 vs 46); across organs; also absent: ARHGAP27; maybe low, not absent |

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (36.0, 4.9); signed map (-5.3, 41.9). **Vector** length 98.5, 22.1% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -2.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +0.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.8 | +0.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.8 | +12.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +0.4 |
|  | [[vincristine (drug)]] 5 µM |  | +1.7 | +0.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.5 | -11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.6 | -15.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -8.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -4.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Ixazomib (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:98,199,011-98,255,649 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PARIS1, TBC1D2A, Armus |
| Gene groups (HGNC) | MicroRNA protein coding host genes; TBC1 domain family members |
| Reactome | 4 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYX2](https://www.uniprot.org/uniprotkb/Q9BYX2) (TBC1 domain family member 2A):

> Acts as a GTPase-activating protein for RAB7A. Signal effector acting as a linker between RAC1 and RAB7A, leading to RAB7A inactivation and subsequent inhibition of cadherin degradation and reduced cell-cell adhesion.

**Summary**, from NCBI Gene [55357](https://www.ncbi.nlm.nih.gov/gene/55357):

> Enables GTPase activator activity and cadherin binding activity. Involved in positive regulation of GTPase activity. Located in cell junction; cytoplasmic vesicle; and cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18026](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18026) · Entrez [55357](https://www.ncbi.nlm.nih.gov/gene/55357) · UniProt [Q9BYX2](https://www.uniprot.org/uniprotkb/Q9BYX2) · Ensembl [ENSG00000095383](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095383)

## Data

Gene col 1744: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1744); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1744, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1744]; `tensor/DDL_lfc|DDL_z.npy` [1744]; `embed/gene_vectors.npy` [1744]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1744 or target_col == 1744). Every well: [[TBC1D2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
