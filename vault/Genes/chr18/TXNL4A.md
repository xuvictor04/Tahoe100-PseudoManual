---
symbol: "TXNL4A"
type: "gene"
col: 6574
ensembl_id: "ENSG00000141759"
name: "thioredoxin like 4A"
location: "18q23"
module: 26
arm: "-"
pooled_cpm: 47.6
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# TXNL4A

*thioredoxin like 4A* — 18q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.47× (z +8.3, q 6e-14, up in 34 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.26× (z +3.5, q 0.024, up in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (Panc 03.27 4.26×, LoVo 2.44×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.680× (z -11.4, q 1e-27, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAP1]] (+0.65, fdr 1e-05), [[ACTR5]] (+0.64, fdr 1e-05), [[CTU2]] (+0.64, fdr 1e-05); moves opposite to [[TLK2]] (-0.63, fdr 2e-05), [[NQO1-DT]] (-0.61, fdr 1e-04), [[MMADHC-DT]] (-0.61, fdr 8e-05).
> It sits in the **-** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[RRP1B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6574.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (Panc 03.27 4.26×, LoVo 2.44×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.47×** | +8.3 | 6e-14 | 34/46 (PANC-1, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.44×** | +7.6 | 1e-11 | 27/42 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +7.0 | 4e-10 | 25/47 (CFPAC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +6.3 | 4e-08 | 31/45 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.27×** | +5.2 | 2e-05 | 29/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.26×** | +5.0 | 5e-05 | 25/48 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.25×** | +4.9 | 9e-05 | 23/48 (NCI-H460, SHP-77, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.24×** | +4.7 | 2e-04 | 20/48 (J82, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.22×** | +4.2 | 0.001 | 20/48 (SHP-77, NCI-H1792, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.024 | 16/48 (NCI-H1573, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.5 | 0.024 | 11/48 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.033 | 13/48 (HCT15, SK-MEL-2, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.046 | 13/48 (SW 900, SNU-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.2 | 0.058 | 7/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.2 | 0.061 | 9/43 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.086 | 4/48 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6574.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.680×** | -11.4 | 1e-27 | 40/48 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.726×** | -9.5 | 8e-19 | 32/47 (A-427, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.779×** | -7.4 | 3e-11 | 29/48 (Hs 766T, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -6.4 | 2e-08 | 30/48 (C32, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.798×** | -4.6 | 4e-04 | 19/48 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.842× | -3.7 | 0.017 | 17/48 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.843× | -3.7 | 0.017 | 17/48 (LS 180, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.845× | -3.7 | 0.018 | 16/48 (C32, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.882× | -3.6 | 0.018 | 15/48 (SNU-1, SW1417, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.850× | -3.4 | 0.038 | 17/47 (hTERT-HPNE, NCI-H23, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.865× | -3.1 | 0.087 | 9/48 (C-33 A, A-427, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.698×** | -3.1 | 0.093 | 10/45 (A498, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.868× | -3.1 | 0.093 | 12/48 (AsPC-1, CHP-212, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.869× | -3.0 | 0.093 | 10/48 (KATO III, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6574. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 51.5 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -13.3) |
| [[HS-578T (line)]] | alt | 63.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -10.6) |
| [[LoVo (line)]] | wt | 60.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -15.1) |
| [[NCI-H460 (line)]] | wt | 40.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -12.4) |
| [[RKO (line)]] | wt | 62.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -9.4) |
| [[SNU-1 (line)]] | wt | 65.7 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.275× (z -12.6) |
| [[SW48 (line)]] | wt | 68.9 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -12.7) |
| [[A-427 (line)]] | wt | 87.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -20.3) |
| [[A498 (line)]] | wt | 35.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.388× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -10.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 59.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -9.9) |
| [[Hs 766T (line)]] | wt | 33.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.420× (z -9.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 67.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 28.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 47.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 24.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 60.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.4) |
| [[SW1417 (line)]] | alt | 41.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -9.2) |
| [[SW480 (line)]] | alt | 27.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -9.5) |
| [[A-172 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 86.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6574), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAP1]] | +0.65 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ACTR5]] | +0.64 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[CTU2]] | +0.64 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[POLRMT]] | +0.63 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TMEM120B]] | +0.63 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[ASB13]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[RSAD1]] | +0.62 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[FAM118A]] | +0.61 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[FAM24B]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[TOMM5]] | +0.61 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[ATAD3B]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[NLE1]] | +0.60 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLK2]] | -0.63 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[NQO1-DT]] | -0.61 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[MMADHC-DT]] | -0.61 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[ZNF341-AS1]] | -0.59 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[CREBBP]] | -0.59 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[CCDC90B-AS1]] | -0.59 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[DNAJB4]] | -0.59 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[PRDM2]] | -0.59 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[TDP2]] | -0.59 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[TMEM202-AS1]] | -0.59 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[PCNX4-DT]] | -0.58 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[EIF4G2]] | -0.58 | -0.50 / -0.41 | both halves | 4e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRP1B]] | C | TXNL4A's natural level weakens RRP1B's drug response | TXNL4A's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.01; direction not clear | 0.090 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **-** arm (projection on the module's main direction -0.559). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-4.7, -26.7); signed map (-45.9, -15.8). **Vector** length 99.5, 23.6% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.9 | +5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +4.4 | +5.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.2 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.0 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.1 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -11.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -6.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -5.2 | -7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -3.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.0 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin like 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q23 — chr18:79,970,813-80,033,949 (-) |
| Ensembl biotype | protein_coding |
| Also known as | U5-15kD, DIM1, HsT161, DIB1, SNRNP15; previously TXNL4 |
| Gene groups (HGNC) | U5 small nuclear ribonucleoprotein |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 8 pathways, smallest: mRNA Splicing - Minor Pathway; mRNA Splicing - Major Pathway; mRNA Splicing |
| Matched by | ensembl_id |

**Function**, from UniProt [P83876](https://www.uniprot.org/uniprotkb/P83876) (Thioredoxin-like protein 4A):

> Plays a role in pre-mRNA splicing as component of the U5 snRNP and U4/U6-U5 tri-snRNP complexes that are involved in spliceosome assembly, and as component of the precatalytic spliceosome (spliceosome B complex).

**Summary**, from NCBI Gene [10907](https://www.ncbi.nlm.nih.gov/gene/10907):

> The protein encoded by this gene is a member of the U5 small ribonucleoprotein particle (snRNP), and is involved in pre-mRNA splicing. This protein contains a thioredoxin-like fold and it is expected to interact with multiple proteins. Protein-protein interactions have been observed with the polyglutamine tract-binding protein 1 (PQBP1). Mutations in both the coding region and promoter region of this gene have been associated with Burn-McKeown syndrome, which is a rare disorder characterized by …

**Accessions** — [HGNC:30551](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30551) · Entrez [10907](https://www.ncbi.nlm.nih.gov/gene/10907) · UniProt [P83876](https://www.uniprot.org/uniprotkb/P83876) · Ensembl [ENSG00000141759](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141759)

## Data

Gene col 6574: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6574); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6574, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6574]; `tensor/DDL_lfc|DDL_z.npy` [6574]; `embed/gene_vectors.npy` [6574]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6574 or target_col == 6574). Every well: [[TXNL4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXNL4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
