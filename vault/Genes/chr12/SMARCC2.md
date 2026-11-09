---
symbol: "SMARCC2"
type: "gene"
col: 6319
ensembl_id: "ENSG00000139613"
name: "SWI/SNF related BAF chromatin remodeling complex subunit C2"
location: "12q13.2"
module: 25
arm: "+"
pooled_cpm: 104.83
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SMARCC2

*SWI/SNF related BAF chromatin remodeling complex subunit C2* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.56× (z +20.7, q 0e+00, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 3.13×, HOP62 3.71×, NCI-H460 2.92×, A498 2.79×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (HOP62 3.86×, PANC-1 3.00×, NCI-H460 3.41×, SW480 2.66×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.633× (z -14.8, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPRIN1]] (+0.59, fdr 3e-05), [[NONO]] (+0.56, fdr 4e-05), [[SYNE2]] (+0.55, fdr 2e-05); moves opposite to [[CIAO2B]] (-0.60, fdr 3e-05), [[ATG101]] (-0.54, fdr 5e-05), [[ZNF143]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6319.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 3.13×, HOP62 3.71×, NCI-H460 2.92×, A498 2.79×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (HOP62 3.86×, PANC-1 3.00×, NCI-H460 3.41×, SW480 2.66×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +20.7 | 0e+00 | 44/44 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +20.2 | 0e+00 | 48/49 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +11.5 | 1e-28 | 38/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | 1.14× | +3.0 | 0.30 | 10/47 (hTERT-HPNE, SW48, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 1.14× | +3.0 | 0.30 | 10/48 (HCT15, A549, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6319.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.633×** | -14.8 | 0e+00 | 38/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.622×** | -10.9 | 5e-25 | 43/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.666×** | -9.3 | 3e-18 | 38/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.775×** | -8.2 | 3e-14 | 33/49 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.729×** | -7.2 | 6e-11 | 35/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.731×** | -7.1 | 9e-11 | 37/48 (SW480, A-427, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.800×** | -5.1 | 3e-05 | 27/48 (SK-MEL-2, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.820×** | -4.5 | 4e-04 | 24/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.820×** | -4.5 | 4e-04 | 25/48 (LOX-IMVI, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.869× | -4.5 | 4e-04 | 17/48 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.845× | -3.8 | 0.007 | 18/48 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.742×** | -3.6 | 0.018 | 18/48 (A-427, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.900× | -3.4 | 0.033 | 9/48 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.904× | -3.2 | 0.048 | 10/48 (SW480, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6319. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 78.2 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.75× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -18.0) |
| [[SW480 (line)]] | alt | 136 | 3 (3 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.66× (z +16.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.403× (z -16.1) |
| [[NCI-H460 (line)]] | wt | 102 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.41× (z +17.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -16.8) |
| [[A-427 (line)]] | wt | 171 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.408× (z -14.1) |
| [[NCI-H2347 (line)]] | alt | 121 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +11.8) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.545× (z -13.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.556× (z -12.8) |
| [[A-172 (line)]] | wt | 103 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +12.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.486× (z -9.4) |
| [[HOP62 (line)]] | alt | 70.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +17.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -11.2) |
| [[Hs 766T (line)]] | wt | 66.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -10.6) |
| [[HS-578T (line)]] | alt | 78.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.91× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.603× (z -8.7) |
| [[J82 (line)]] | alt | 115 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -11.8) |
| [[LS 180 (line)]] | wt | 108 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.72× (z +12.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.481× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 106 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -13.4) |
| [[NCI-H23 (line)]] | alt | 140 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -11.1) |
| [[A498 (line)]] | wt | 96.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +14.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 123 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +12.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.411× (z -9.8) |
| [[C32 (line)]] | wt | 81.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 73.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -10.4) |
| [[HCT15 (line)]] | alt | 149 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 138 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +14.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 91.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -13.7) |
| [[LOX-IMVI (line)]] | wt | 103 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 104 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +14.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 167 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -12.0) |
| [[PANC-1 (line)]] | alt | 115 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +18.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 91.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +13.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 102 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +14.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 86.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 85.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +11.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 83.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +11.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 97.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +11.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.415× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 55.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +14.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 97.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 109 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -10.2) |
| [[SNU-1 (line)]] | wt | 118 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -11.2) |
| [[SW 900 (line)]] | alt | 77.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -11.1) |
| [[AN3 CA (line)]] | alt | 138 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.4) |
| [[BT-474 (line)]] | alt | 93.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.453× (z -9.1) |
| [[CHP-212 (line)]] | wt | 81.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +8.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 89.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +11.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 73.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 141 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.131× (z -12.8) |
| [[RKO (line)]] | wt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +11.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 140 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6319), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPRIN1]] | +0.59 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[NONO]] | +0.56 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[SYNE2]] | +0.55 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[DCTN1]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[EXOC5]] | +0.55 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[RAD23B]] | +0.54 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[ZC3H14]] | +0.54 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[PCM1]] | +0.54 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[AP3M1]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[KAT7]] | +0.53 | +0.51 / +0.56 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[STAG2]] | +0.53 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[SUDS3]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |

## Genes that move opposite

*49 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO2B]] | -0.60 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[ATG101]] | -0.54 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[ZNF143]] | -0.53 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[ALG2]] | -0.53 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[GTF2B]] | -0.53 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[CDC20-DT]] | -0.53 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[KCNK6]] | -0.52 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[COX7A2]] ⚠ | -0.52 | -0.40 / -0.58 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NOP10]] ⚠ | -0.52 | -0.28 / -0.59 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MFSD2A]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[BLZF1]] | -0.51 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[BET1L]] | -0.51 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[RABGEF1]] | -0.51 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[TFAP2E]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SMARCC2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.574). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.4, -23.2); signed map (-19.7, -37.1). **Vector** length 93.6, 24.8% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +20.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +20.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -1.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.0 | +1.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +2.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.4 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -3.9 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.1 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.4 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -0.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.2 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | SWI/SNF related BAF chromatin remodeling complex subunit C2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:56,162,359-56,189,567 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BAF170, Rsc8, CRACC2 |
| Gene groups (HGNC) | Myb/SANT domain containing; BAF complex subunits; PBAF complex subunits |
| Reactome | 21 pathways, smallest: Formation of the non-canonical BAF (ncBAF) complex; Formation of the polybromo-BAF (pBAF) complex; Formation of the embryonic stem cell BAF (esBAF) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAQ2](https://www.uniprot.org/uniprotkb/Q8TAQ2) (SWI/SNF complex subunit SMARCC2):

> Involved in transcriptional activation and repression of select genes by chromatin remodeling (alteration of DNA-nucleosome topology). Component of SWI/SNF chromatin remodeling complexes that carry out key enzymatic activities, changing chromatin structure by altering DNA-histone contacts within a nucleosome in an ATP-dependent manner. Can stimulate the ATPase activity of the catalytic subunit of these complexes. May be required for CoREST dependent repression of neuronal specific gene …

**Summary**, from NCBI Gene [6601](https://www.ncbi.nlm.nih.gov/gene/6601):

> The protein encoded by this gene is a member of the SWI/SNF family of proteins, whose members display helicase and ATPase activities and which are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI and contains a predicted leucine zipper motif typical of many transcription factors. Alternatively spliced transcript variants encoding different …

**Accessions** — [HGNC:11105](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11105) · Entrez [6601](https://www.ncbi.nlm.nih.gov/gene/6601) · UniProt [Q8TAQ2](https://www.uniprot.org/uniprotkb/Q8TAQ2) · Ensembl [ENSG00000139613](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139613)

## Data

Gene col 6319: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6319); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6319, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6319]; `tensor/DDL_lfc|DDL_z.npy` [6319]; `embed/gene_vectors.npy` [6319]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6319 or target_col == 6319). Every well: [[SMARCC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMARCC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
