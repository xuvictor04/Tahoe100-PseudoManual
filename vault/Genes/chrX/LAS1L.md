---
symbol: "LAS1L"
type: "gene"
col: 10
ensembl_id: "ENSG00000001497"
name: "LAS1 like ribosome biogenesis factor"
location: "Xq12"
module: 4
arm: "+"
pooled_cpm: 33.83
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# LAS1L

*LAS1 like ribosome biogenesis factor* — Xq12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.10× (z +20.7, q 0e+00, up in 44 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.50× (z +7.4, q 8e-12, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.702× (z -6.5, q 5e-08, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.260×; ⚠ cell-cycle shift, explains ~74% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.436×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.491×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYBBP1A]] (+0.80, fdr 7e-06), [[FARSB]] (+0.78, fdr 7e-06), [[RUVBL1]] (+0.77, fdr 7e-06); moves opposite to [[DCTN6-DT]] (-0.68, fdr 7e-06), [[ZNF821]] (-0.67, fdr 7e-06), [[RSRP1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SHOX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 20 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.10×** | +20.7 | 0e+00 | 44/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.91×** | +18.7 | 0e+00 | 37/40 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.21×** | +13.4 | 1e-38 | 40/42 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.00×** | +12.6 | 2e-34 | 45/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.83×** | +10.9 | 1e-25 | 42/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.81×** | +10.8 | 4e-25 | 42/48 (HOP62, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +7.4 | 8e-12 | 30/47 (HT-29, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +7.3 | 2e-11 | 32/48 (A549, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.15×** | +7.3 | 2e-11 | 34/48 (PANC-1, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +6.1 | 7e-08 | 28/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +6.1 | 7e-08 | 1/48 (H4) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.40×** | +5.9 | 2e-07 | 25/48 (NCI-H1573, A549, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +5.5 | 2e-06 | 24/47 (NCI-H460, A549, …) | all doses, flat | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.34×** | +5.2 | 7e-06 | 25/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.22×** | +5.2 | 7e-06 | 23/47 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.1 | 1e-05 | 26/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +4.7 | 8e-05 | 21/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.5 | 2e-04 | 17/48 (HOP62, NCI-H1573, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +4.3 | 5e-04 | 20/48 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.1 | 9e-04 | 19/48 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.003 | 17/48 (SNU-423, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 5 µM |  | 1.15× | +3.6 | 0.007 | 11/48 (SW480, RKO, …) | top dose only | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.011 | 12/48 (SW1417, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.015 | 14/48 (C-33 A, SW480, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.018 | 7/48 (SW1417, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.260×; ⚠ cell-cycle shift, explains ~74% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Panc 03.27 0.436×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.491×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.702×** | -6.5 | 5e-08 | 30/48 (SNU-423, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.828×** | -4.9 | 3e-04 | 24/48 (SNU-1, HEC-1-A, …) | two highest doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.836× | -3.3 | 0.14 | 8/48 (RPMI-7951, PANC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.882× | -3.3 | 0.14 | 11/48 (HEC-1-A, KATO III, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.833× | -3.2 | 0.14 | 17/47 (A-427, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 32.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.66× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 40.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 43.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.21× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Selinexor (drug)]] 5 µM 0.491× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 44.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HT-29 (line)]] | alt | 24.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LOX-IMVI (line)]] | wt | 27.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 39.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[PANC-1 (line)]] | alt | 43.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 41.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A549 (line)]] | wt | 32.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 44.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LoVo (line)]] | wt | 21.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2347 (line)]] | alt | 19.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[Panc 03.27 (line)]] | alt | 32.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 59.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 23.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.62× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[BT-474 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -10.2) ⚠ cell-cycle shift, explains ~74% of this change |
| [[CFPAC-1 (line)]] | alt | 17.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HEC-1-A (line)]] | alt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[Hs 766T (line)]] | wt | 31.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[KATO III (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 23.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1792 (line)]] | alt | 13.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2030 (line)]] | alt | 19.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H23 (line)]] | alt | 77.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[RKO (line)]] | wt | 42.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW 900 (line)]] | alt | 21.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.0) ⚠ cell-cycle shift, explains ~86% of this change | — |
| [[AN3 CA (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYBBP1A]] | +0.80 | +0.77 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 507 |
| [[FARSB]] | +0.78 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[RUVBL1]] | +0.77 | +0.76 / +0.76 | both halves | 7e-06 | STRING 902 |
| [[ELAC2]] | +0.75 | +0.67 / +0.76 | both halves | 7e-06 | pathway: rRNA processing; STRING 469 |
| [[EFTUD2]] | +0.75 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[NUP155]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.73 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[NOM1]] | +0.73 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[NOC2L]] | +0.73 | +0.66 / +0.73 | both halves | 7e-06 | STRING 663 |
| [[PFAS]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[EIF2S1]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[PUM3]] | +0.70 | +0.70 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN6-DT]] | -0.68 | -0.65 / -0.71 | both halves | 7e-06 |  |
| [[ZNF821]] | -0.67 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.64 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[ZMAT5]] | -0.64 | -0.46 / -0.70 | both halves | 3e-05 |  |
| [[SNHG9]] | -0.62 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[AKAP1-DT]] | -0.61 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[ACAP1]] | -0.61 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[COX7B]] | -0.61 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[RABAC1]] | -0.61 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[HOTAIRM1]] | -0.60 | -0.53 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SHOX2]] | B | SHOX2 activity raises LAS1L's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without SHOX2 | 0.089 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.784). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.8, -34.1); signed map (-7.5, -45.9). **Vector** length 91.5, 22.1% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.50 to 21); *tRNA processing in the nucleus* (reactome, mean cos +0.50 to 8); *Folding of actin by CCT/TriC* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +5.8 | +20.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +5.8 | +18.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +5.7 | +13.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +4.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +5.1 |
| fall | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.0 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | LAS1 like ribosome biogenesis factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq12 — chrX:65,438,549-65,534,810 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12525, Las1 |
| Gene groups (HGNC) | Large ribosomal subunit biogenesis complex |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4W2](https://www.uniprot.org/uniprotkb/Q9Y4W2) (Ribosomal biogenesis protein LAS1L):

> Required for the synthesis of the 60S ribosomal subunit and maturation of the 28S rRNA. Functions as a component of the Five Friends of Methylated CHTOP (5FMC) complex; the 5FMC complex is recruited to ZNF148 by methylated CHTOP, leading to desumoylation of ZNF148 and subsequent transactivation of ZNF148 target genes. Required for the efficient pre-rRNA processing at both ends of internal transcribed spacer 2 (ITS2).

**Summary**, from NCBI Gene [81887](https://www.ncbi.nlm.nih.gov/gene/81887):

> Enables RNA binding activity. Involved in rRNA processing. Located in nucleolus. Part of MLL1 complex. Implicated in Wilson-Turner syndrome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25726) · Entrez [81887](https://www.ncbi.nlm.nih.gov/gene/81887) · UniProt [Q9Y4W2](https://www.uniprot.org/uniprotkb/Q9Y4W2) · Ensembl [ENSG00000001497](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000001497)

## Data

Gene col 10: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10]; `tensor/DDL_lfc|DDL_z.npy` [10]; `embed/gene_vectors.npy` [10]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10 or target_col == 10). Every well: [[LAS1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAS1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
