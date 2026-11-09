---
symbol: "C1S"
type: "gene"
col: 11276
ensembl_id: "ENSG00000182326"
name: "complement C1s"
location: "12p13.31"
module: 23
arm: "+"
pooled_cpm: 49.33
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# C1S

*complement C1s* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.13× (z +29.3, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.474× (z -15.5, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFHX2-AS1]] (+0.80, fdr 1e-05), [[CFAP53]] (+0.77, fdr 7e-06), [[CASS4]] (+0.74, fdr 1e-05); moves opposite to [[FAM102B]] (-0.66, fdr 1e-05), [[BTBD3]] (-0.65, fdr 1e-05), [[REPS1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11276.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.13×** | +29.3 | 0e+00 | 44/47 (HOP62, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +26.4 | 0e+00 | 45/47 (HOP62, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.39×** | +25.5 | 0e+00 | 37/46 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.04×** | +14.8 | 0e+00 | 37/46 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +11.4 | 3e-28 | 35/47 (HOP62, SW1417, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +11.1 | 1e-26 | 30/47 (Panc 03.27, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +10.7 | 1e-24 | 32/47 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +5.8 | 4e-07 | 22/47 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.8 | 8e-05 | 20/44 (LOX-IMVI, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +4.4 | 7e-04 | 21/48 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.49×** | +4.3 | 1e-03 | 12/46 (HEC-1-A, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.004 | 17/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.7 | 0.009 | 10/46 (SNU-1, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.010 | 18/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.014 | 14/47 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Gefitinib (drug)]] 5 µM |  | 1.18× | +3.4 | 0.027 | 7/47 (A-427, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.036 | 12/45 (LoVo, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.043 | 11/47 (C-33 A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11276.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.474×** | -15.5 | 0e+00 | 42/47 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.579×** | -11.3 | 2e-27 | 38/47 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.614×** | -10.1 | 7e-22 | 35/47 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.628×** | -9.7 | 6e-20 | 32/46 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.453×** | -8.6 | 9e-16 | 35/47 (LoVo, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.663×** | -8.5 | 1e-15 | 30/47 (RPMI-7951, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | **0.783×** | -5.1 | 3e-05 | 18/45 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.856× | -4.6 | 3e-04 | 18/48 (SW480, C-33 A, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.850× | -3.4 | 0.043 | 17/47 (SNU-423, HS-578T, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.847× | -3.3 | 0.059 | 11/46 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Bexarotene (drug)]] 0.5 µM |  | 0.856× | -3.3 | 0.059 | 7/47 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Bexarotene (drug)]] 5 µM |  | 0.862× | -3.1 | 0.089 | 3/47 (SW480, KATO III, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.903× | -3.0 | 0.11 | 14/47 (NCI-H460, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11276. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 45.8 | 6 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +19.0) | [[Docetaxel (drug)]] 0.05 µM 0.370× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~15% of this change |
| [[NCI-H460 (line)]] | wt | 37.8 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +21.1) | [[Belinostat (drug)]] 5 µM 0.399× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 29.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +23.0) | — |
| [[SW480 (line)]] | alt | 59.2 | 4 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.76× (z +15.8) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.415× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 41.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +14.8) | — |
| [[C32 (line)]] | wt | 23.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +24.1) | — |
| [[LoVo (line)]] | wt | 92.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 47.6 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.328× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 24.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.61× (z +21.7) | — |
| [[NCI-H23 (line)]] | alt | 71.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +19.7) | — |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.264× (z -11.7) |
| [[SW48 (line)]] | wt | 36.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 53.2 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.89× (z +13.4) | — |
| [[HS-578T (line)]] | alt | 72.4 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.276× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 73.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +14.5) | — |
| [[NCI-H1792 (line)]] | alt | 77.5 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +15.8) | [[Belinostat (drug)]] 5 µM 0.260× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 29.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +15.8) | — |
| [[PANC-1 (line)]] | alt | 20.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +13.1) | — |
| [[RKO (line)]] | wt | 53.8 | 1 | 2 | [[Auranofin (drug)]] 5 µM 3.33× (z +8.5) | [[Belinostat (drug)]] 5 µM 0.264× (z -9.5) |
| [[SW1417 (line)]] | alt | 15.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.47× (z +12.8) | — |
| [[CHP-212 (line)]] | wt | 61.3 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.104× (z -10.8) ⚠ toxic · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.124× (z -9.6) |
| [[COLO 205 (line)]] | alt | 38.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +11.9) | — |
| [[H4 (line)]] | wt | 178 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.05× (z +9.1) | [[Belinostat (drug)]] 5 µM 0.335× (z -9.0) |
| [[HCT15 (line)]] | alt | 94.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 25.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +12.3) | — |
| [[HT-29 (line)]] | alt | 22.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 12.4× (z +16.4) | — |
| [[LS 180 (line)]] | wt | 23.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +12.5) | — |
| [[NCI-H2347 (line)]] | alt | 14.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +14.6) | — |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +14.3) | — |
| [[SW 900 (line)]] | alt | 28.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +15.1) | — |
| [[A-427 (line)]] | wt | 29.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.36× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 13.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.85× (z +13.9) | — |
| [[CFPAC-1 (line)]] | alt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 61.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +11.6) | — |
| [[J82 (line)]] | alt | 75.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 31.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 44.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 53.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.235× (z -10.0) |
| [[SW 1088 (line)]] | alt | 155 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.109× (z -9.0) |
| [[A-172 (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11276), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFHX2-AS1]] | +0.80 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.77 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[CASS4]] | +0.74 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[CHD1-DT]] | +0.74 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[LINC02936]] | +0.74 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[DENND6A-AS1]] | +0.73 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[ST8SIA5]] | +0.73 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.72 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[TBCE-1]] | +0.72 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[LINC00880]] | +0.71 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.71 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[MSH4]] | +0.71 | +0.67 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM102B]] | -0.66 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[BTBD3]] | -0.65 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[REPS1]] | -0.65 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[INPP5F]] | -0.64 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[SPATA6]] | -0.63 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[PAFAH1B3]] | -0.63 | -0.53 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C1S's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises C1S's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[JAM2]] | B | JAM2 activity raises C1S's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 1.65× lower at baseline in the lines without JAM2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[LINC01358]] | B | LINC01358 activity strengthens C1S's drug response | lines that do not express LINC01358 (14) vs lines expressing it (33) | the lines without LINC01358 respond 0.86× as strongly (z diff +0.19); strongest at Belinostat 5 µM: 0.57x vs 0.42x (z diff +2.5) | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, BMPER, FRMD4A; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[PLS1]] | B | PLS1 activity lowers C1S's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 1.79× higher at baseline in the lines without PLS1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (26.8, -15.3); signed map (21.3, -0.6). **Vector** length 130, 36.4% of its response variance represented; |z| ≥ 3 in 1,277 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.2 | +29.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.1 | +26.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +10.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.4 | +11.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +1.9 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +2.5 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -9.5 | -15.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -8.3 | -11.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.4 | -9.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.4 | -10.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.0 | -8.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -6.3 | -8.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.3 | -1.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.8 | -3.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.6 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | complement C1s |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,988,259-7,071,032 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Serine proteases; Sushi domain containing; Complement system activation components |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, COAGULATION, COMPLEMENT, INTERFERON_GAMMA_RESPONSE |
| Reactome | 9 pathways, smallest: Creation of C4 and C2 activators; Initial triggering of complement; Regulation of Complement cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [P09871](https://www.uniprot.org/uniprotkb/P09871) (Complement C1s subcomponent):

> Component of the complement C1 complex, a multiprotein complex that initiates the classical pathway of the complement system, a cascade of proteins that leads to phagocytosis and breakdown of pathogens and signaling that strengthens the adaptive immune system. C1S is activated following association of the C1 complex with immunoglobulins (IgG or IgM) complexed with antigens to form antigen-antibody complexes on the surface of pathogens. C1S is cleaved and activated by C1R to generate C1s …

**Summary**, from NCBI Gene [716](https://www.ncbi.nlm.nih.gov/gene/716):

> This gene encodes a serine protease, which is a major constituent of the human complement subcomponent C1. C1s associates with two other complement components C1r and C1q in order to yield the first component of the serum complement system. Defects in this gene are the cause of selective C1s deficiency. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:1247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1247) · Entrez [716](https://www.ncbi.nlm.nih.gov/gene/716) · UniProt [P09871](https://www.uniprot.org/uniprotkb/P09871) · Ensembl [ENSG00000182326](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182326)

## Data

Gene col 11276: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11276); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11276, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11276]; `tensor/DDL_lfc|DDL_z.npy` [11276]; `embed/gene_vectors.npy` [11276]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11276 or target_col == 11276). Every well: [[C1S — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1S.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
