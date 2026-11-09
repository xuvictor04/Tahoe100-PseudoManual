---
symbol: "TNK2"
type: "gene"
col: 705
ensembl_id: "ENSG00000061938"
name: "tyrosine kinase non receptor 2"
location: "3q29"
module: 2
arm: "+"
pooled_cpm: 30.58
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 27
n_dd_up_clean: 10
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TNK2

*tyrosine kinase non receptor 2* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.31× (z +16.6, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.503× (z -19.2, q 0e+00, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.433× (z -16.5, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAMSAP1]] (+0.73, fdr 1e-05), [[CEP131]] (+0.72, fdr 2e-05), [[DVL1]] (+0.72, fdr 1e-05); moves opposite to [[PNISR-AS1]] (-0.67, fdr 7e-05), [[ERCC6L2]] (-0.66, fdr 3e-05), [[MCPH1]] (-0.63, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[HGD]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 705.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +16.6 | 0e+00 | 41/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +13.8 | 6e-41 | 39/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +11.6 | 1e-28 | 38/48 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +7.7 | 2e-12 | 37/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +7.0 | 4e-10 | 26/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +6.6 | 3e-09 | 30/48 (SW480, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +5.6 | 2e-06 | 21/47 (HepG2/C3A, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.32×** | +5.2 | 2e-05 | 18/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +4.6 | 2e-04 | 19/47 (SW480, SW48, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.26×** | +4.5 | 3e-04 | 11/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.5 | 0.025 | 14/48 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.046 | 11/45 (SW480, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.2 | 0.059 | 5/48 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +3.1 | 0.075 | 4/48 (NCI-H1792, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 705.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.503×** | -19.2 | 0e+00 | 39/47 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.433×** | -16.5 | 0e+00 | 45/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.467×** | -15.0 | 0e+00 | 42/47 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.511×** | -13.2 | 8e-38 | 35/47 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.549×** | -11.8 | 4e-30 | 43/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.586×** | -10.5 | 6e-24 | 34/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.564×** | -10.5 | 9e-24 | 33/48 (LoVo, HOP62, …) | rises with dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.386×** | -9.8 | 7e-21 | 38/48 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.687×** | -7.4 | 9e-12 | 29/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.496×** | -7.2 | 3e-11 | 28/40 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.540×** | -6.3 | 1e-08 | 25/47 (LOX-IMVI, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.732×** | -6.1 | 4e-08 | 23/48 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.735×** | -6.1 | 6e-08 | 22/47 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.730×** | -5.8 | 2e-07 | 21/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.749×** | -5.7 | 5e-07 | 22/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.590×** | -5.4 | 2e-06 | 19/48 (PANC-1, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -4.9 | 3e-05 | 22/48 (SK-MEL-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.792×** | -4.6 | 1e-04 | 23/48 (PANC-1, A-172, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.855× | -4.3 | 4e-04 | 18/48 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.665×** | -4.2 | 7e-04 | 19/48 (HCT15, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 705. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 33.9 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.28× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -12.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 30.1 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.167× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 37.8 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.07× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -24.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 34.9 | 1 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.49× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -12.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.333× (z -11.1) |
| [[SW480 (line)]] | alt | 53.0 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.26× (z +10.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.361× (z -12.7) |
| [[Hs 766T (line)]] | wt | 41.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -11.0) |
| [[HS-578T (line)]] | alt | 29.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -9.8) |
| [[A-172 (line)]] | wt | 44.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -17.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -11.5) |
| [[AN3 CA (line)]] | alt | 26.6 | 0 | 3 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0934× (z -9.0) ⚠ toxic · without an alert: [[Finasteride (drug)]] 0.05 µM 0.0823× (z -8.8) |
| [[HOP62 (line)]] | alt | 25.6 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 28.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 42.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -13.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -12.1) |
| [[SNU-1 (line)]] | wt | 29.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -11.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -11.2) |
| [[A-427 (line)]] | wt | 37.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -9.5) |
| [[A498 (line)]] | wt | 21.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -11.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -10.5) |
| [[HCT15 (line)]] | alt | 23.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.06× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.144× (z -10.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 28.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0671× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 22.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -9.2) |
| [[RKO (line)]] | wt | 21.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.89× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -13.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -16.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 19.0 | 0 | 1 | — | [[Auranofin (drug)]] 0.05 µM 0.0653× (z -8.9) |
| [[COLO 205 (line)]] | alt | 61.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.269× (z -10.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 29.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.79× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.508× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 51.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.328× (z -9.5) |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 705), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMSAP1]] | +0.73 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[CEP131]] | +0.72 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[DVL1]] | +0.72 | +0.68 / +0.49 | both halves | 1e-05 | same gene group |
| [[GNAI2]] | +0.71 | +0.57 / +0.47 | both halves | 2e-05 | same gene group |
| [[ANKRD27]] | +0.70 | +0.65 / +0.39 | both halves | 6e-05 |  |
| [[SH3GLB2]] | +0.69 | +0.62 / +0.51 | both halves | 1e-05 | same gene group |
| [[PEDS1]] | +0.69 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[KIAA0930]] | +0.68 | +0.51 / +0.58 | both halves | 1e-05 | same gene group |
| [[PPP1R12C]] | +0.67 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[MAST3]] | +0.67 | +0.61 / +0.32 | both halves | 2e-04 |  |
| [[TCF3]] | +0.67 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[SUN1]] | +0.66 | +0.54 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNISR-AS1]] | -0.67 | -0.62 / -0.38 | both halves | 7e-05 |  |
| [[ERCC6L2]] | -0.66 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[MCPH1]] | -0.63 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[MFF-DT]] | -0.63 | -0.53 / -0.20 | both halves | 7e-04 |  |
| [[ZNF24]] | -0.63 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[ERCC6L2-AS1]] | -0.62 | -0.59 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |
| [[PBLD]] | -0.62 | -0.59 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[CCDC90B-AS1]] | -0.61 | -0.60 / -0.06 | ⚠ one half (not replicated) | 0.004 |  |
| [[RFX3-DT]] | -0.61 | -0.58 / -0.12 | ⚠ one half (not replicated) | 0.002 |  |
| [[THAP2]] | -0.61 | -0.57 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[DECR1]] | -0.61 | -0.62 / -0.29 | both halves | 3e-04 |  |
| [[CASD1]] | -0.60 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[NSUN3]] | -0.59 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[LATS1]] | -0.59 | -0.45 / -0.26 | both halves | 4e-04 |  |
| [[YARS2]] | -0.59 | -0.41 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HGD]] | B | HGD activity lowers TNK2's level | lines that do not express HGD (15) vs lines expressing it (35) | 1.24× higher at baseline in the lines without HGD | 0.033 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[MEGF6]] | B | MEGF6 activity raises TNK2's level | lines that do not express MEGF6 (11) vs lines expressing it (39) | 1.47× lower at baseline in the lines without MEGF6 | 0.035 | ⚠ within organs, on part of the lines; also absent: SQOR; maybe low, not absent |
| [[ARHGAP45]] | B | ARHGAP45 activity raises TNK2's level | lines that do not express ARHGAP45 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without ARHGAP45 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TNK2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TNK2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[BAIAP3]] | B | BAIAP3 activity raises TNK2's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 1.23× lower at baseline in the lines without BAIAP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent; its own permutation p |
| [[RBKS]] | B | RBKS activity raises TNK2's level | lines that do not express RBKS (6) vs lines expressing it (44) | 1.13× lower at baseline in the lines without RBKS | 0.091 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RTN4R]] | C | RTN4R activity raises TNK2's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without RTN4R | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.746). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (5.7, -1.1); signed map (-40.7, -5.6). **Vector** length 82.6, 18.2% of its response variance represented; |z| ≥ 3 in 1,284 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.1 | +11.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.8 | +16.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.4 | +13.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.5 | +7.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.4 | +5.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +6.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +7.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -6.6 | -5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.4 | -19.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -13.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -6.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | +0.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | tyrosine kinase non receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:195,863,364-195,911,945 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p21cdc42Hs, ACK, ACK1 |
| Gene groups (HGNC) | TNK family tyrosine kinases; MicroRNA protein coding host genes; SH3 domain containing |
| Reactome | 2 pathways, smallest: Signaling by LTK; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07912](https://www.uniprot.org/uniprotkb/Q07912) (Activated CDC42 kinase 1):

> Non-receptor tyrosine-protein and serine/threonine-protein kinase that is implicated in cell spreading and migration, cell survival, cell growth and proliferation. Transduces extracellular signals to cytosolic and nuclear effectors. Phosphorylates AKT1, AR, MCF2, WASL and WWOX. Implicated in trafficking and clathrin-mediated endocytosis through binding to epidermal growth factor receptor (EGFR) and clathrin. Binds to both poly- and mono-ubiquitin and regulates ligand-induced degradation of …

**Summary**, from NCBI Gene [10188](https://www.ncbi.nlm.nih.gov/gene/10188):

> This gene encodes a tyrosine kinase that binds Cdc42Hs in its GTP-bound form and inhibits both the intrinsic and GTPase-activating protein (GAP)-stimulated GTPase activity of Cdc42Hs. This binding is mediated by a unique sequence of 47 amino acids C-terminal to an SH3 domain. The protein may be involved in a regulatory mechanism that sustains the GTP-bound active form of Cdc42Hs and which is directly linked to a tyrosine phosphorylation signal transduction pathway. Several alternatively spliced …

**Accessions** — [HGNC:19297](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19297) · Entrez [10188](https://www.ncbi.nlm.nih.gov/gene/10188) · UniProt [Q07912](https://www.uniprot.org/uniprotkb/Q07912) · Ensembl [ENSG00000061938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000061938)

## Data

Gene col 705: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 705); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 705, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 705]; `tensor/DDL_lfc|DDL_z.npy` [705]; `embed/gene_vectors.npy` [705]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 705 or target_col == 705). Every well: [[TNK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
