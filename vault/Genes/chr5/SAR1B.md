---
symbol: "SAR1B"
type: "gene"
col: 7652
ensembl_id: "ENSG00000152700"
name: "secretion associated Ras related GTPase 1B"
location: "5q31.1"
module: 42
arm: "+"
pooled_cpm: 65.72
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SAR1B

*secretion associated Ras related GTPase 1B* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.15× (z +19.3, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.945× (z -4.2, q 0.016, down in 1 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Temsirolimus (drug)]] 0.05 µM: 0.823× (z -3.8, q 0.036, down in 19 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (SW 900 0.0859×; ⚠ toxic); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SW 1271 0.267×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.136×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSR1]] (+0.61, fdr 1e-05), [[UFSP2]] (+0.59, fdr 1e-05), [[SEC63]] (+0.59, fdr 1e-05); moves opposite to [[NR2C2AP]] (-0.57, fdr 2e-05), [[RPP25]] (-0.55, fdr 3e-04), [[NOP56]] (-0.52, fdr 5e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TUBA4A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7652.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +19.3 | 0e+00 | 44/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.05×** | +14.4 | 1e-44 | 46/49 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +11.1 | 3e-26 | 40/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.75×** | +11.0 | 4e-26 | 35/49 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +10.9 | 2e-25 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +10.2 | 2e-22 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.65×** | +9.5 | 2e-19 | 27/41 (CFPAC-1, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +9.1 | 7e-18 | 38/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +8.3 | 5e-15 | 37/45 (CFPAC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +8.3 | 5e-15 | 34/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +8.0 | 6e-14 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.46×** | +7.5 | 3e-12 | 35/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +7.2 | 2e-11 | 37/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +7.1 | 5e-11 | 32/47 (CFPAC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +7.1 | 6e-11 | 32/48 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +6.8 | 5e-10 | 35/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +6.3 | 1e-08 | 32/48 (SW480, RPMI-7951, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +4.4 | 4e-04 | 25/48 (CFPAC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.004 | 21/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.008 | 19/49 (MIA PaCa-2, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7652.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (SW 900 0.0859×; ⚠ toxic); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SW 1271 0.267×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.136×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -4.2 | 0.016 | 1/50 (NCI-H661) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.823×** | -3.8 | 0.036 | 19/49 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.829×** | -3.7 | 0.044 | 17/49 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.841× | -3.4 | 0.063 | 13/48 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.842× | -3.4 | 0.063 | 16/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.843× | -3.4 | 0.063 | 15/48 (LoVo, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.876× | -3.3 | 0.063 | 17/48 (SW 1271, Panc 03.27, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.846× | -3.3 | 0.063 | 14/48 (COLO 205, LS 180, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.840× | -3.3 | 0.063 | 19/48 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.850× | -3.2 | 0.072 | 10/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.875× | -3.2 | 0.072 | 11/48 (AsPC-1, H4, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.876× | -3.1 | 0.077 | 19/48 (NCI-H1792, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.854× | -3.1 | 0.077 | 14/49 (CFPAC-1, LoVo, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.854× | -3.1 | 0.077 | 10/48 (LoVo, CFPAC-1, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.857× | -3.0 | 0.091 | 14/47 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.858× | -3.0 | 0.093 | 15/49 (HT-29, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7652. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 56.3 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +15.6) | — |
| [[NCI-H460 (line)]] | wt | 65.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +26.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 48.3 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +17.0) | — |
| [[NCI-H1573 (line)]] | alt | 74.0 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +22.9) | — |
| [[CFPAC-1 (line)]] | alt | 94.8 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.42× (z +18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 62.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.2) | — |
| [[A-172 (line)]] | wt | 54.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +12.3) | — |
| [[HOP62 (line)]] | alt | 62.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 63.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.7) | — |
| [[BT-474 (line)]] | alt | 74.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[C32 (line)]] | wt | 55.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +14.7) | — |
| [[LoVo (line)]] | wt | 84.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 33.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[C-33 A (line)]] | alt | 30.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.86× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 88.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +17.1) | — |
| [[NCI-H1792 (line)]] | alt | 49.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.08× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 45.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 72.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 77.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.7) | — |
| [[SNU-423 (line)]] | alt | 56.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +22.8) | — |
| [[SW 900 (line)]] | alt | 51.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.7) | [[Lonafarnib (drug)]] 5 µM 0.0859× (z -11.1) ⚠ toxic |
| [[A-427 (line)]] | wt | 50.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.2) | — |
| [[A549 (line)]] | wt | 58.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.5) | — |
| [[AsPC-1 (line)]] | alt | 88.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.86× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 52.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.136× (z -8.7) |
| [[COLO 205 (line)]] | alt | 85.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 83.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.49× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 66.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.6) | — |
| [[RKO (line)]] | wt | 47.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.7) | — |
| [[SHP-77 (line)]] | alt | 52.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.267× (z -9.2) |
| [[SW48 (line)]] | wt | 47.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +9.5) | — |
| [[A498 (line)]] | wt | 96.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7652), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSR1]] | +0.61 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[UFSP2]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SEC63]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[COPG1]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[STT3A]] | +0.59 | +0.45 / +0.63 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[DAP]] | +0.57 | +0.36 / +0.59 | both halves | 9e-05 |  |
| [[SEC22B]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation; STRING 787 |
| [[ARL1]] | +0.55 | +0.56 / +0.43 | both halves | 3e-05 | same gene group |
| [[MCEE]] | +0.55 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[SRPRA]] | +0.54 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[TMEM39A]] | +0.54 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[SLC30A5]] | +0.53 | +0.59 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2C2AP]] | -0.57 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[RPP25]] | -0.55 | -0.29 / -0.59 | both halves | 3e-04 |  |
| [[NOP56]] | -0.52 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[FMNL2]] | -0.49 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[NOP16]] | -0.49 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[NINL]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[BOK]] | -0.48 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[POLR1G]] | -0.48 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[LRFN4]] | -0.48 | -0.26 / -0.57 | both halves | 4e-04 |  |
| [[DIAPH2]] | -0.47 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[TUBA4A]] | -0.47 | -0.32 / -0.47 | both halves | 2e-04 | pathway: Asparagine N-linked glycosylation |
| [[ABHD15]] | -0.47 | -0.23 / -0.50 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TUBA4A]] | B | TUBA4A activity raises SAR1B's level | lines that do not express TUBA4A (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without TUBA4A | 0.038 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| [[ZNF600]] | B | ZNF600 activity raises SAR1B's level | lines that do not express ZNF600 (9) vs lines expressing it (41) | 1.21× lower at baseline in the lines without ZNF600 | 0.050 | ⚠ within organs, on part of the lines; also absent: ZNF320, ZNF28, ZNF468 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.536). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.9, -36.4); signed map (-55.2, 10.0). **Vector** length 94.0, 25.9% of its response variance represented; |z| ≥ 3 in 1,088 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.9 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.3 | +9.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +14.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.1 | +0.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.0 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +1.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.9 | -3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | +2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -0.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.4 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | secretion associated Ras related GTPase 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:134,601,149-134,649,271 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SARA2 |
| Gene groups (HGNC) | ARF GTPase family; Coat protein complex II |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 23 pathways, smallest: Chylomicron assembly; Plasma lipoprotein assembly; Antigen Presentation: Folding, assembly and peptide loading of class I MHC |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6B6](https://www.uniprot.org/uniprotkb/Q9Y6B6) (Small COPII coat GTPase SAR1B):

> Small GTPase that cycles between an active GTP-bound and an inactive GDP-bound state and mainly functions in vesicle-mediated endoplasmic reticulum (ER) to Golgi transport. The active GTP-bound form inserts into the endoplasmic reticulum membrane where it recruits the remainder of the coat protein complex II/COPII. The coat protein complex II assembling and polymerizing on endoplasmic reticulum membrane is responsible for both the sorting of cargos and the deformation and budding of membranes …

**Summary**, from NCBI Gene [51128](https://www.ncbi.nlm.nih.gov/gene/51128):

> The protein encoded by this gene is a small GTPase that acts as a homodimer. The encoded protein is activated by the guanine nucleotide exchange factor PREB and is involved in protein transport from the endoplasmic reticulum to the Golgi. This protein is part of the COPII coat complex. Defects in this gene are a cause of chylomicron retention disease (CMRD), also known as Anderson disease (ANDD). Two transcript variants encoding the same protein have been found for this gene. [provided by …

**Accessions** — [HGNC:10535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10535) · Entrez [51128](https://www.ncbi.nlm.nih.gov/gene/51128) · UniProt [Q9Y6B6](https://www.uniprot.org/uniprotkb/Q9Y6B6) · Ensembl [ENSG00000152700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152700)

## Data

Gene col 7652: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7652); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7652, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7652]; `tensor/DDL_lfc|DDL_z.npy` [7652]; `embed/gene_vectors.npy` [7652]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7652 or target_col == 7652). Every well: [[SAR1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAR1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
