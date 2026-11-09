---
symbol: "CTSC"
type: "gene"
col: 3089
ensembl_id: "ENSG00000109861"
name: "cathepsin C"
location: "11q14.2"
module: 12
arm: "-"
pooled_cpm: 67.84
n_lines_expressing: 45
n_dd_up: 29
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CTSC

*cathepsin C* — 11q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.94× (z +27.3, q 0e+00, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.765× (z -4.6, q 0.002, down in 20 of 42 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 0.814× (z -3.7, q 0.033, down in 15 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA4]] (+0.58, fdr 1e-05), [[TM4SF18]] (+0.58, fdr 1e-04), [[LAMB1]] (+0.53, fdr 1e-05); moves opposite to [[BCAS2]] (-0.58, fdr 1e-05), [[RBMX2]] (-0.55, fdr 3e-05), [[BTBD6]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[ZNF205]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 20 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3089.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.94×** | +27.3 | 0e+00 | 41/43 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.74×** | +18.0 | 0e+00 | 34/41 (A498, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.69×** | +17.0 | 0e+00 | 31/35 (HT-29, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.14×** | +12.6 | 4e-34 | 28/38 (HS-578T, J82, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +12.4 | 2e-33 | 35/43 (SW1417, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.77×** | +10.2 | 2e-22 | 30/42 (C32, HS-578T, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.72×** | +9.6 | 4e-20 | 32/43 (LOX-IMVI, C32, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.73×** | +9.4 | 4e-19 | 30/45 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.66×** | +9.0 | 1e-17 | 27/43 (LOX-IMVI, C32, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.65×** | +9.0 | 2e-17 | 32/43 (C32, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.62×** | +8.3 | 8e-15 | 29/42 (HEC-1-A, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +8.0 | 6e-14 | 30/43 (SW1417, HT-29, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +7.5 | 4e-12 | 30/43 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.51×** | +7.0 | 8e-11 | 26/42 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **1.38×** | +5.5 | 1e-06 | 23/42 (NCI-H1792, C32, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.64×** | +4.6 | 1e-04 | 21/43 (SW1417, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.2 | 9e-04 | 17/43 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.006 | 16/43 (AsPC-1, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.006 | 15/43 (SW1417, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.010 | 16/43 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.023 | 11/43 (HS-578T, SW480, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.043 | 6/43 (HS-578T, C32, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.080 | 8/41 (AsPC-1, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.35×** | +2.8 | 0.085 | 17/43 (AsPC-1, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | 1.17× | +2.8 | 0.085 | 6/43 (BT-474, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3089.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.765×** | -4.6 | 0.002 | 20/42 (NCI-H2030, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.759×** | -4.5 | 0.002 | 20/45 (NCI-H460, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.798×** | -3.8 | 0.027 | 18/43 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.814×** | -3.7 | 0.033 | 15/43 (KATO III, hTERT-HPNE, …) | top dose only |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.808×** | -3.6 | 0.036 | 13/43 (HepG2/C3A, SNU-423, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.870× | -3.4 | 0.057 | 11/43 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.821×** | -3.4 | 0.058 | 17/42 (J82, A498, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | 0.879× | -3.3 | 0.077 | 10/43 (KATO III, RPMI-7951, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.880× | -3.2 | 0.077 | 11/44 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -3.2 | 0.077 | 4/45 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.837× | -3.2 | 0.077 | 12/42 (NCI-H2030, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.077 | 13/42 (HepG2/C3A, NCI-H23, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.721×** | -3.1 | 0.098 | 14/45 (NCI-H460, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.888× | -3.0 | 0.11 | 15/43 (CFPAC-1, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3089. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 41.0 | 8 (7 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 78.1 | 6 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.68× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 98.1 | 6 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 52.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +12.1) | — |
| [[NCI-H460 (line)]] | wt | 421 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -16.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.305× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 38.3 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.59× (z +26.3) | — |
| [[HOP62 (line)]] | alt | 19.9 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +15.8) | — |
| [[A498 (line)]] | wt | 70.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[CFPAC-1 (line)]] | alt | 28.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +15.7) | — |
| [[HT-29 (line)]] | alt | 31.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.01× (z +18.2) | — |
| [[J82 (line)]] | alt | 59.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +14.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 85.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 35.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +17.2) | — |
| [[PANC-1 (line)]] | alt | 54.8 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +15.4) | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 41.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +15.9) | — |
| [[A549 (line)]] | wt | 25.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +12.3) | — |
| [[KATO III (line)]] | alt | 40.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +15.3) | — |
| [[NCI-H2030 (line)]] | alt | 58.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 60.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 41.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +16.3) | — |
| [[A-427 (line)]] | wt | 55.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.79× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 31.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.59× (z +18.1) | — |
| [[COLO 205 (line)]] | alt | 25.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 40.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 32.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 88.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +16.5) | — |
| [[SNU-1 (line)]] | wt | 28.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +11.2) | — |
| [[SW48 (line)]] | wt | 41.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 74.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +10.1) | — |
| [[A-172 (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 77.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 103 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3089), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA4]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TM4SF18]] | +0.58 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[LAMB1]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[NEMP2]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[PRPS2]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CHN1]] | +0.52 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[SLC39A8]] | +0.51 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[FUCA2]] | +0.51 | +0.48 / +0.33 | both halves | 1e-04 |  |
| [[SLC16A2]] | +0.51 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[COL4A6]] | +0.50 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[QPCT]] | +0.49 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[STAMBPL1]] | +0.49 | +0.49 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAS2]] | -0.58 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[RBMX2]] | -0.55 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[BTBD6]] | -0.55 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[UBE2B]] | -0.55 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[IK]] | -0.54 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[FRG1]] | -0.54 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SSNA1]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[DNAJB2]] | -0.53 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[TSR3]] | -0.53 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[NOL7]] ⚠ | -0.53 | -0.50 / -0.43 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CREB3]] | -0.52 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[PRPF6]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ZNF205]] | -0.51 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF205]] | B | CTSC activity lowers ZNF205's level | lines that do not express CTSC (5) vs lines expressing it (45) | 1.31× higher at baseline in the lines without CTSC | 0.085 | ⚠ within organs, on part of the lines; maybe low, not absent |
| cells under [[γ-Oryzanol (drug)]] 0.05 µM | B | CTSC activity raises the cells' numbers under γ-Oryzanol 0.05 µM (protects the cells) | lines that do not express CTSC (5) vs lines expressing it (43) | the lines without CTSC: 0.84× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (44.7, 30.9); signed map (45.5, 40.9). **Vector** length 115, 31.7% of its response variance represented; |z| ≥ 3 in 1,224 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.5 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +27.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +6.3 | +17.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +6.2 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +3.7 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.1 | -4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | -3.0 | -3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.9 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | +0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -0.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | cathepsin C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.2 — chr11:88,265,069-88,359,684 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DPP1; previously PLS, PALS |
| Gene groups (HGNC) | Cathepsins |
| Hallmark sets | PROTEIN_SECRETION, COMPLEMENT, MTORC1_SIGNALING |
| Reactome | 14 pathways, smallest: Cargo concentration in the ER; COPII-mediated vesicle transport; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P53634](https://www.uniprot.org/uniprotkb/P53634) (Dipeptidyl peptidase 1):

> Thiol protease. Has dipeptidylpeptidase activity. Active against a broad range of dipeptide substrates composed of both polar and hydrophobic amino acids. Proline cannot occupy the P1 position and arginine cannot occupy the P2 position of the substrate. Can act as both an exopeptidase and endopeptidase. Activates serine proteases such as elastase, cathepsin G and granzymes A and B.

**Summary**, from NCBI Gene [1075](https://www.ncbi.nlm.nih.gov/gene/1075):

> This gene encodes a member of the peptidase C1 family and lysosomal cysteine proteinase that appears to be a central coordinator for activation of many serine proteinases in cells of the immune system. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate heavy and light chains that form a disulfide-linked dimer. A portion of the propeptide acts as an intramolecular chaperone for the folding and …

**Accessions** — [HGNC:2528](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2528) · Entrez [1075](https://www.ncbi.nlm.nih.gov/gene/1075) · UniProt [P53634](https://www.uniprot.org/uniprotkb/P53634) · Ensembl [ENSG00000109861](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109861)

## Data

Gene col 3089: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3089); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3089, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3089]; `tensor/DDL_lfc|DDL_z.npy` [3089]; `embed/gene_vectors.npy` [3089]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3089 or target_col == 3089). Every well: [[CTSC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTSC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
