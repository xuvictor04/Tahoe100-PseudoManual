---
symbol: "POLD3"
type: "gene"
col: 1191
ensembl_id: "ENSG00000077514"
name: "DNA polymerase delta 3, accessory subunit"
location: "11q13.4"
module: 6
arm: "+"
pooled_cpm: 50.41
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# POLD3

*DNA polymerase delta 3, accessory subunit* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.81× (z +11.9, q 7e-30, up in 37 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.22× (z +3.9, q 0.005, up in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 12 lines (LoVo 5.53×, CFPAC-1 7.14×, Panc 03.27 3.98×, C32 4.41×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 3.00×, NCI-H1573 2.71×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW480 2.42×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 1.67×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (CFPAC-1 3.25×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.532× (z -12.6, q 2e-33, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXO1]] (+0.82, fdr 7e-06), [[CENPU]] (+0.81, fdr 7e-06), [[MCM10]] (+0.81, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 15 with an alert ⚠; shown: the 15 strongest. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1191.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 12 lines (LoVo 5.53×, CFPAC-1 7.14×, Panc 03.27 3.98×, C32 4.41×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 3.00×, NCI-H1573 2.71×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW480 2.42×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 1.67×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (CFPAC-1 3.25×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.81×** | +11.9 | 7e-30 | 37/46 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.82×** | +11.5 | 2e-28 | 30/41 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.52×** | +7.8 | 1e-12 | 27/42 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +5.8 | 8e-07 | 21/48 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.21×** | +5.4 | 6e-06 | 21/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.19× | +4.9 | 1e-04 | 17/48 (SW480, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +4.8 | 1e-04 | 17/48 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.26×** | +4.7 | 2e-04 | 23/48 (PANC-1, SW480, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +4.5 | 4e-04 | 18/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.26×** | +4.5 | 5e-04 | 20/48 (SW480, HS-578T, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.15× | +4.0 | 0.003 | 12/49 (SW480, HT-29, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.005 | 15/48 (A498, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.20× | +3.6 | 0.015 | 13/48 (C32, SNU-423, …) | two highest doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 1.19× | +3.5 | 0.020 | 10/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | 1.18× | +3.3 | 0.039 | 12/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.532×** | -12.6 | 2e-33 | 40/48 (COLO 205, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.718×** | -9.4 | 2e-18 | 30/48 (A-427, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.744×** | -8.3 | 1e-14 | 37/48 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.759×** | -5.5 | 6e-06 | 26/48 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.762×** | -5.4 | 7e-06 | 23/47 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -4.8 | 1e-04 | 21/47 (A498, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.845× | -4.7 | 2e-04 | 16/48 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.781×** | -4.6 | 2e-04 | 22/48 (KATO III, A-427, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.735×** | -4.4 | 7e-04 | 21/48 (SW480, A-172, …) | two highest doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.826×** | -3.6 | 0.017 | 15/48 (Panc 03.27, NCI-H23, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 0.837× | -3.5 | 0.021 | 19/48 (A498, A-427, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.842× | -3.4 | 0.028 | 17/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.721×** | -3.4 | 0.029 | 13/45 (HEC-1-A, A-427, …) | top dose only | noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.839× | -3.3 | 0.038 | 11/48 (C32, AN3 CA, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.743×** | -3.1 | 0.066 | 8/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.856× | -3.1 | 0.066 | 16/48 (NCI-H1573, C32, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.743×** | -3.1 | 0.066 | 15/48 (SNU-423, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 50.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 53.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.14× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.25× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 57.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -17.1) |
| [[KATO III (line)]] | alt | 72.8 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.285× (z -9.9) |
| [[SW480 (line)]] | alt | 55.5 | 2 (2 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.42× (z +10.0) ⚠ toxic; cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.376× (z -11.6) |
| [[A-427 (line)]] | wt | 79.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -17.3) |
| [[C-33 A (line)]] | alt | 76.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | [[Auranofin (drug)]] 5 µM 0.304× (z -11.3) |
| [[C32 (line)]] | wt | 41.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.41× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[H4 (line)]] | wt | 41.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.26× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.0) |
| [[HOP62 (line)]] | alt | 31.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[LoVo (line)]] | wt | 27.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.53× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[Panc 03.27 (line)]] | alt | 62.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | [[Auranofin (drug)]] 5 µM 0.336× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 29.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.44× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[BT-474 (line)]] | alt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.18× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[HEC-1-A (line)]] | alt | 64.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.385× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.96× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 26.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.162× (z -9.6) |
| [[J82 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.475× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[LS 180 (line)]] | wt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 52.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[NCI-H23 (line)]] | alt | 109 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.406× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 43.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[PANC-1 (line)]] | alt | 53.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.473× (z -8.5) |
| [[SHP-77 (line)]] | alt | 134 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 37.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -9.0) |
| [[A-172 (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXO1]] | +0.82 | +0.81 / +0.81 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins; STRING 759 |
| [[CENPU]] | +0.81 | +0.82 / +0.77 | both halves | 7e-06 | pathway: Chromosome Maintenance |
| [[MCM10]] | +0.81 | +0.82 / +0.78 | both halves | 7e-06 | pathway: DNA Replication; STRING 434 |
| [[RRM1]] | +0.81 | +0.75 / +0.83 | both halves | 7e-06 | STRING 436 |
| [[WDHD1]] | +0.81 | +0.76 / +0.81 | both halves | 7e-06 |  |
| [[WDR76]] | +0.80 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[CDC45]] | +0.79 | +0.78 / +0.78 | both halves | 7e-06 | pathway: DNA Replication; STRING 456 |
| [[ORC1]] | +0.79 | +0.79 / +0.77 | both halves | 7e-06 | pathway: DNA Replication |
| [[MMS22L]] | +0.79 | +0.78 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MCM4]] | +0.79 | +0.75 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 456 |
| [[CLSPN]] | +0.79 | +0.77 / +0.78 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair |
| [[MCM2]] | +0.79 | +0.71 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers POLD3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM111B]] | B | FAM111B activity raises POLD3's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.43× lower at baseline in the lines without FAM111B | 0.095 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.837). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.5, -45.6); signed map (-38.1, -43.6). **Vector** length 121, 33.7% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F G1/S* (control, mean cos +0.68 to 23); *Cell Cycle Checkpoints* (reactome, mean cos +0.69 to 45); *Activation of the pre-replicative complex* (reactome, mean cos +0.70 to 22).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +4.8 | +4.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +4.1 | +4.5 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +4.0 | +5.4 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.9 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +3.4 | +3.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.9 | +2.4 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.8 | +2.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.3 | -12.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.6 | -8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -6.0 | -5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | -4.0 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.3 | -3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase delta 3, accessory subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:74,493,851-74,669,117 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P66, KIAA0039, P68, PPP1R128 |
| Gene groups (HGNC) | DNA polymerases; Protein phosphatase 1 regulatory subunits |
| Hallmark sets | DNA_REPAIR, E2F_TARGETS |
| Reactome | 47 pathways, smallest: Leading Strand Synthesis; Mismatch repair (MMR) directed by MSH2:MSH3 (MutSbeta); Mismatch repair (MMR) directed by MSH2:MSH6 (MutSalpha) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15054](https://www.uniprot.org/uniprotkb/Q15054) (DNA polymerase delta subunit 3):

> Accessory component of both the DNA polymerase delta complex and the DNA polymerase zeta complex. As a component of the trimeric and tetrameric DNA polymerase delta complexes (Pol-delta3 and Pol-delta4, respectively), plays a role in high fidelity genome replication, including in lagging strand synthesis, and repair. Required for optimal Pol-delta activity. Stabilizes the Pol-delta complex and plays a major role in Pol-delta stimulation by PCNA. Pol-delta3 and Pol-delta4 are characterized by …

**Summary**, from NCBI Gene [10714](https://www.ncbi.nlm.nih.gov/gene/10714):

> This gene encodes the 66-kDa subunit of DNA polymerase delta. DNA polymerase delta possesses both polymerase and 3' to 5' exonuclease activity and plays a critical role in DNA replication and repair. The encoded protein plays a role in regulating the activity of DNA polymerase delta through interactions with other subunits and the processivity cofactor proliferating cell nuclear antigen (PCNA). Alternatively spliced transcript variants have been observed for this gene. [provided by RefSeq, Mar …

**Accessions** — [HGNC:20932](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20932) · Entrez [10714](https://www.ncbi.nlm.nih.gov/gene/10714) · UniProt [Q15054](https://www.uniprot.org/uniprotkb/Q15054) · Ensembl [ENSG00000077514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077514)

## Data

Gene col 1191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1191); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1191]; `tensor/DDL_lfc|DDL_z.npy` [1191]; `embed/gene_vectors.npy` [1191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1191 or target_col == 1191). Every well: [[POLD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
