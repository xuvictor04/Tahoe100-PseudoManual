---
symbol: "DHRS2"
type: "gene"
col: 2033
ensembl_id: "ENSG00000100867"
name: "dehydrogenase/reductase 2"
location: "14q11.2"
module: 15
arm: "-"
pooled_cpm: 13.47
n_lines_expressing: 37
n_dd_up: 27
n_dd_down: 18
n_dd_up_clean: 22
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# DHRS2

*dehydrogenase/reductase 2* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.96× (z +22.4, q 0e+00, up in 26 of 27 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 20.8× (z +20.9, q 0e+00, up in 33 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Cytarabine (hydrochloride) (drug)]] 0.5 µM: 0.401× (z -6.3, q 2e-07, down in 18 of 33 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.577× (z -5.3, q 2e-05, down in 19 of 31 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBBP4-1]] (+0.64, fdr 2e-05), [[TCN2]] (+0.60, fdr 1e-05), [[ANKRD20A9P]] (+0.59, fdr 1e-05); moves opposite to [[GARS1-DT]] (-0.62, fdr 2e-05), [[SAP30L-AS1]] (-0.61, fdr 2e-04), [[PRDM10]] (-0.60, fdr 5e-05).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SYP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2033.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **9.96×** | +22.4 | 0e+00 | 26/27 (HepG2/C3A, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **20.8×** | +20.9 | 0e+00 | 33/33 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **18.2×** | +20.0 | 0e+00 | 34/34 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **9.67×** | +15.7 | 0e+00 | 31/33 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **10.4×** | +15.5 | 0e+00 | 29/31 (SNU-1, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **7.34×** | +13.8 | 5e-41 | 31/33 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.63×** | +12.6 | 2e-34 | 30/34 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.13×** | +12.5 | 5e-34 | 21/28 (SNU-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.99×** | +11.1 | 9e-27 | 30/34 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.97×** | +9.5 | 1e-19 | 15/22 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **3.72×** | +9.1 | 6e-18 | 27/32 (LOX-IMVI, SW48, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.93×** | +7.1 | 4e-11 | 7/12 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **2.83×** | +6.6 | 1e-09 | 22/30 (A-427, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **2.26×** | +5.6 | 7e-07 | 13/34 (HepG2/C3A, SNU-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.12×** | +5.2 | 8e-06 | 16/32 (LOX-IMVI, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.21×** | +4.2 | 9e-04 | 15/33 (BT-474, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.55×** | +4.1 | 0.001 | 11/30 (hTERT-HPNE, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.72×** | +3.8 | 0.006 | 4/34 (CFPAC-1, SNU-423, …) | top dose only | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.74×** | +3.6 | 0.008 | 7/30 (HepG2/C3A, SNU-1, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2033.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.401×** | -6.3 | 2e-07 | 18/33 (NCI-H23, HEC-1-A, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.577×** | -5.3 | 2e-05 | 19/31 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.581×** | -5.3 | 2e-05 | 20/34 (CFPAC-1, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.463×** | -5.1 | 5e-05 | 15/32 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.593×** | -4.8 | 2e-04 | 15/34 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.515×** | -4.6 | 5e-04 | 15/34 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.519×** | -4.5 | 5e-04 | 14/32 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.512×** | -4.4 | 7e-04 | 15/32 (Panc 03.27, HEC-1-A, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.531×** | -4.4 | 8e-04 | 14/32 (HEC-1-A, SW1417, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.515×** | -4.2 | 0.001 | 12/32 (HEC-1-A, CFPAC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.579×** | -3.7 | 0.009 | 9/32 (LS 180, SNU-1, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | **0.576×** | -3.6 | 0.013 | 10/32 (SK-MEL-2, LOX-IMVI, …) | top dose only |  |
| [[Trifluridine (drug)]] 5 µM |  | **0.693×** | -3.6 | 0.016 | 14/32 (HEC-1-A, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trifluridine (drug)]] 0.5 µM |  | **0.620×** | -3.3 | 0.042 | 6/32 (H4, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **0.625×** | -3.2 | 0.047 | 13/33 (SW48, LS 180, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM |  | **0.632×** | -3.2 | 0.058 | 10/32 (AN3 CA, SW1417, …) | inconsistent across doses | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **0.728×** | -3.1 | 0.069 | 15/32 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.650×** | -3.0 | 0.098 | 12/34 (SW480, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +1.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2033. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.7 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 61.0× (z +14.4) | — |
| [[HepG2_C3A (line)]] | wt | 289 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +19.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.84× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 30.8 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +14.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.7× (z +9.9) | [[Selinexor (drug)]] 5 µM 0.208× (z -8.7) ⚠ cell-cycle shift, explains ~89% of this change |
| [[A549 (line)]] | wt | 9.95 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 52.2× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 8.59 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +13.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 15.3× (z +9.2) | — |
| [[KATO III (line)]] | alt | 13.8 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 34.2× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 20.2 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 20.7× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 47.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 16.2× (z +13.9) | — |
| [[HEC-1-A (line)]] | alt | 61.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +10.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 7.06× (z +9.5) | — |
| [[LoVo (line)]] | wt | 4.26 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +10.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 23.9× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 4.37 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.6× (z +9.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 79.9× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 45.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +10.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 9.31× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 22.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +11.1) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[Panc 03.27 (line)]] | alt | 9.21 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +9.6) ⚠ cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0533× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0785× (z -8.7) ⚠ cell-cycle shift, explains ~89% of this change |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.7× (z +10.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H2030 (line)]] | alt | 3.75 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 62.8× (z +11.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 24.6× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 5.47 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +8.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW48 (line)]] | wt | 17.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 34.1× (z +12.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2033), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBBP4-1]] | +0.64 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[TCN2]] | +0.60 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[ANKRD20A9P]] | +0.59 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[H3-3B]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SNAPIN]] | +0.58 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[KLF2]] | +0.57 | +0.43 / +0.39 | both halves | 5e-05 |  |
| [[POTEF]] | +0.57 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[IER2]] | +0.56 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[AACSP1]] | +0.54 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[FAR2P1]] | +0.54 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[ANKRD20A8P]] | +0.53 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[LINC00624]] | +0.53 | +0.63 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARS1-DT]] | -0.62 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[SAP30L-AS1]] | -0.61 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[PRDM10]] | -0.60 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[GLUD1P3]] | -0.58 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[CDK2AP1]] | -0.58 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[MCM9]] | -0.57 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[FBXO22]] | -0.57 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[TMEM11-DT]] | -0.57 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[NAF1]] | -0.57 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[METTL4]] | -0.56 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[GTF3C2-AS2]] | -0.56 | -0.12 / -0.49 | ⚠ not reproduced | 0.002 |  |
| [[ZNF460-AS1]] | -0.56 | -0.21 / -0.50 | both halves | 7e-04 |  |
| [[DIDO1]] | -0.56 | -0.40 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DHRS2's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAR2P1]], [[POTEF]] | B | FAR2P1, POTEF activity raises DHRS2's level | lines that do not express FAR2P1, POTEF (29) vs lines expressing them (21) | 2.84× lower at baseline in the lines without FAR2P1, POTEF | 0.018 | ⚠ within organs, on part of the lines; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent genes |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYP]] | B | DHRS2 activity raises SYP's level | lines that do not express DHRS2 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without DHRS2 | 0.096 | ⚠ within organs, on part of the lines; also absent: MAN1C1 |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.8, 23.6); signed map (33.2, 36.0). **Vector** length 82.2, 19.2% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +12.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +13.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.4 | +15.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +20.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.1 | +20.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +9.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +6.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | -0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.6 | -0.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -5.3 | -5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -0.4 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.8 | -4.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | dehydrogenase/reductase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:23,630,115-23,645,639 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HEP27, SDR25C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13268](https://www.uniprot.org/uniprotkb/Q13268) (Dehydrogenase/reductase SDR family member 2, mitochondrial):

> NADPH-dependent oxidoreductase which catalyzes the reduction of dicarbonyl compounds. Displays reductase activity in vitro with 3,4-hexanedione, 2,3-heptanedione and 1-phenyl-1,2-propanedione as substrates. May function as a dicarbonyl reductase in the enzymatic inactivation of reactive carbonyls involved in covalent modification of cellular components. Also displays a minor hydroxysteroid dehydrogenase activity toward bile acids such as ursodeoxycholic acid (UDCA) and isoursodeoxycholic acid …

**Summary**, from NCBI Gene [10202](https://www.ncbi.nlm.nih.gov/gene/10202):

> This gene encodes a member of the short-chain dehydrogenases/reductases (SDR) family, which has over 46,000 members. Members of this family are enzymes that metabolize many different compounds, such as steroid hormones, prostaglandins, retinoids, lipids and xenobiotics. Alternative promoter use and alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2017]

**Accessions** — [HGNC:18349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18349) · Entrez [10202](https://www.ncbi.nlm.nih.gov/gene/10202) · UniProt [Q13268](https://www.uniprot.org/uniprotkb/Q13268) · Ensembl [ENSG00000100867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100867)

## Data

Gene col 2033: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2033); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2033, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2033]; `tensor/DDL_lfc|DDL_z.npy` [2033]; `embed/gene_vectors.npy` [2033]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2033 or target_col == 2033). Every well: [[DHRS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHRS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
