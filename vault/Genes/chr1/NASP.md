---
symbol: "NASP"
type: "gene"
col: 5370
ensembl_id: "ENSG00000132780"
name: "nuclear autoantigenic sperm protein"
location: "1p34.1"
module: 6
arm: "+"
pooled_cpm: 119.36
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# NASP

*nuclear autoantigenic sperm protein* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.05× (z +14.7, q 0e+00, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.24× (z +4.4, q 5e-04, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.802× (z -4.6, q 0.003, down in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~94% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 4 lines (A-427 0.342×, A498 0.512×, LS 180 0.536×, A-172 0.531×; ⚠ cell-cycle shift, explains ~94% of this change); [[Sunitinib (drug)]] 5 µM in 1 line (SW 1088 0.106×; ⚠ toxic); [[XRK3F2 (drug)]] 0.5 µM in 1 line (CHP-212 0.104×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRIP1]] (+0.72, fdr 7e-06), [[SMC1A]] (+0.72, fdr 7e-06), [[ATAD2]] (+0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 19 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5370.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.05×** | +14.7 | 0e+00 | 42/48 (AsPC-1, HS-578T, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.59×** | +9.4 | 1e-18 | 41/49 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.77×** | +8.2 | 4e-14 | 40/48 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.71×** | +7.5 | 1e-11 | 38/48 (J82, AsPC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.67×** | +7.3 | 2e-11 | 38/48 (J82, H4, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.61×** | +6.8 | 8e-10 | 41/48 (A549, AsPC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.0 | 1e-07 | 1/50 (C32) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.48×** | +5.6 | 2e-06 | 34/49 (A549, NCI-H460, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | **1.47×** | +5.4 | 5e-06 | 34/47 (HS-578T, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.39×** | +4.7 | 1e-04 | 33/48 (NCI-H460, H4, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.4 | 5e-04 | 28/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +4.2 | 0.001 | 28/48 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.33×** | +4.0 | 0.003 | 30/50 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.32×** | +3.9 | 0.003 | 25/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.32×** | +3.7 | 0.008 | 26/45 (RPMI-7951, HT-29, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.010 | 29/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.034 | 26/48 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5370.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 4 lines (A-427 0.342×, A498 0.512×, LS 180 0.536×, A-172 0.531×; ⚠ cell-cycle shift, explains ~94% of this change); [[Sunitinib (drug)]] 5 µM in 1 line (SW 1088 0.106×; ⚠ toxic); [[XRK3F2 (drug)]] 0.5 µM in 1 line (CHP-212 0.104×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.802×** | -4.6 | 0.003 | 27/48 (A-427, A498, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.749×** | -4.1 | 0.014 | 31/47 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.841× | -3.6 | 0.063 | 19/48 (KATO III, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.856× | -3.2 | 0.22 | 17/48 (A-427, NCI-H23, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 0.863× | -3.1 | 0.25 | 13/48 (RKO, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 53.4 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +22.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 81.8 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 208 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 146 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +11.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 119 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.8) ⚠ cell-cycle shift, explains ~32% of this change | [[Selinexor (drug)]] 5 µM 0.512× (z -10.0) ⚠ cell-cycle shift, explains ~94% of this change |
| [[A549 (line)]] | wt | 76.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 91.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +18.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[C32 (line)]] | wt | 122 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +15.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 132 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.16× (z +10.6) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[HOP62 (line)]] | alt | 115 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 84.6 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 87.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 115 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +14.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 67.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +18.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[Panc 03.27 (line)]] | alt | 132 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[RPMI-7951 (line)]] | alt | 94.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +12.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW 900 (line)]] | alt | 91.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +15.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 78.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.531× (z -8.7) ⚠ cell-cycle shift, explains ~94% of this change |
| [[A-427 (line)]] | wt | 173 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.342× (z -16.5) ⚠ cell-cycle shift, explains ~94% of this change |
| [[CFPAC-1 (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +17.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[CHP-212 (line)]] | wt | 66.6 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.104× (z -8.6) |
| [[COLO 205 (line)]] | alt | 91.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +13.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HepG2_C3A (line)]] | wt | 74.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 87.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +19.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 90.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +12.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 132 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.536× (z -9.1) ⚠ cell-cycle shift, explains ~94% of this change |
| [[NCI-H1573 (line)]] | alt | 66.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +15.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2347 (line)]] | alt | 97.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[PANC-1 (line)]] | alt | 160 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +11.0) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 132 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +15.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 99.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +14.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW 1088 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.106× (z -8.9) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 224 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 239 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 137 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 135 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 73.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRIP1]] | +0.72 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[SMC1A]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[ATAD2]] | +0.71 | +0.65 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 447 |
| [[BRCA1]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[HELLS]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 556 |
| [[EZH2]] | +0.68 | +0.62 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CENPH]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[E2F8]] | +0.67 | +0.56 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[ESCO2]] | +0.66 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.66 | +0.58 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 510 |
| [[FAM111B]] | +0.66 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[MCM4]] | +0.66 | +0.60 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 599 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NASP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[E2F8]] | B | E2F8 activity raises NASP's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.62× lower at baseline in the lines without E2F8 | 0.063 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises NASP's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without E2F2 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises NASP's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.83× lower at baseline in the lines without AURKB | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises NASP's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without MCM10 | 0.049 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises NASP's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 1.89× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[CLSPN]] | C | CLSPN activity raises NASP's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without CLSPN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; its own permutation p |
| [[C21orf58]], [[CDC45]] | C | C21orf58, CDC45 activity raises NASP's level | lines that do not express C21orf58, CDC45 (3) vs lines expressing them (47) | 1.82× lower at baseline in the lines without C21orf58, CDC45 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises NASP's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 1.83× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.070 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent genes |
| [[MYBL2]] | C | MYBL2 activity raises NASP's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 1.68× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.5, -43.0); signed map (-36.9, -48.2). **Vector** length 125, 44.4% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.52 to 28); *DNA Replication* (reactome, mean cos +0.51 to 40); *E2F G1/S* (control, mean cos +0.56 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.2 | +14.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +3.0 | +4.0 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.0 | +3.1 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +3.0 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.9 | +9.4 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.9 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | +2.7 | +0.8 |
|  | [[Methotrexate (drug)]] 0.5 µM |  | +2.7 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | -7.3 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.2 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -6.6 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.7 | -1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.4 | +0.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | nuclear autoantigenic sperm protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,583,846-45,618,904 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLB7527, FLJ31599, FLJ35510, MGC19722, MGC20372, MGC2297, DKFZp547F162, PRO1999 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Hallmark sets | GLYCOLYSIS, G2M_CHECKPOINT, E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [P49321](https://www.uniprot.org/uniprotkb/P49321) (Nuclear autoantigenic sperm protein):

> Component of the histone chaperone network. Binds and stabilizes histone H3-H4 not bound to chromatin to maintain a soluble reservoir and modulate degradation by chaperone-mediated autophagy. Required for DNA replication, normal cell cycle progression and cell proliferation. Forms a cytoplasmic complex with HSP90 and H1 linker histones and stimulates HSP90 ATPase activity. NASP and H1 histone are subsequently released from the complex and translocate to the nucleus where the histone is released …

**Summary**, from NCBI Gene [4678](https://www.ncbi.nlm.nih.gov/gene/4678):

> This gene encodes a H1 histone binding protein that is involved in transporting histones into the nucleus of dividing cells. Multiple isoforms are encoded by transcript variants of this gene. The somatic form is expressed in all mitotic cells, is localized to the nucleus, and is coupled to the cell cycle. The testicular form is expressed in embryonic tissues, tumor cells, and the testis. In male germ cells, this protein is localized to the cytoplasm of primary spermatocytes, the nucleus of …

**Accessions** — [HGNC:7644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7644) · Entrez [4678](https://www.ncbi.nlm.nih.gov/gene/4678) · UniProt [P49321](https://www.uniprot.org/uniprotkb/P49321) · Ensembl [ENSG00000132780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132780)

## Data

Gene col 5370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5370); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5370]; `tensor/DDL_lfc|DDL_z.npy` [5370]; `embed/gene_vectors.npy` [5370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5370 or target_col == 5370). Every well: [[NASP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NASP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
