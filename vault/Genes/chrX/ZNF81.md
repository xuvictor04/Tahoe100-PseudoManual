---
symbol: "ZNF81"
type: "gene"
col: 12462
ensembl_id: "ENSG00000197779"
name: "zinc finger protein 81"
location: "Xp11.23"
module: 16
arm: "+"
pooled_cpm: 19.51
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZNF81

*zinc finger protein 81* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.39× (z +13.4, q 2e-38, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.649× (z -6.7, q 1e-08, down in 27 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.653× (z -6.6, q 1e-08, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (SW480 0.261×, SHP-77 0.173×, NCI-H1792 0.196×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (BT-474 0.116×, A-172 0.189×, C32 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H460 0.279×, SW480 0.325×); [[Drospirenone (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0961×); [[Cinacalcet (drug)]] 0.5 µM in 1 line (AN3 CA 0.0642×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERCC4]] (+0.61, fdr 1e-05), [[SLC35A4]] (+0.61, fdr 1e-05), [[ZKSCAN2]] (+0.60, fdr 1e-05); moves opposite to [[GTF2IP4]] (-0.57, fdr 3e-05), [[KMT5C]] (-0.56, fdr 1e-05), [[GIT1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12462.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.39×** | +13.4 | 2e-38 | 44/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +12.5 | 3e-33 | 40/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.16×** | +11.9 | 3e-30 | 41/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.13×** | +11.7 | 3e-29 | 41/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +10.7 | 8e-25 | 39/47 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +8.6 | 5e-16 | 38/48 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +7.0 | 3e-10 | 28/48 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +6.7 | 2e-09 | 30/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +6.2 | 5e-08 | 29/47 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.31×** | +5.9 | 2e-07 | 24/48 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.93×** | +5.3 | 5e-06 | 19/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.1 | 2e-05 | 20/48 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.41×** | +5.0 | 2e-05 | 23/46 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.34×** | +4.5 | 3e-04 | 18/47 (SNU-1, LS 180, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.32×** | +4.2 | 8e-04 | 18/47 (MIA PaCa-2, A549, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.017 | 9/47 (RKO, SNU-423, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.017 | 10/47 (RKO, NCI-H1573, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +2.9 | 0.086 | 10/48 (RKO, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12462.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (SW480 0.261×, SHP-77 0.173×, NCI-H1792 0.196×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (BT-474 0.116×, A-172 0.189×, C32 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H460 0.279×, SW480 0.325×); [[Drospirenone (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0961×); [[Cinacalcet (drug)]] 0.5 µM in 1 line (AN3 CA 0.0642×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.649×** | -6.7 | 1e-08 | 27/46 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.653×** | -6.6 | 1e-08 | 27/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.710×** | -5.1 | 7e-05 | 24/46 (HepG2/C3A, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.642×** | -3.6 | 0.047 | 17/44 (RPMI-7951, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.810× | -3.3 | 0.12 | 20/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~80% of this change | 0.814× | -3.2 | 0.13 | 12/43 (KATO III, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.824× | -3.0 | 0.22 | 17/47 (NCI-H460, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12462. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 18.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 30.1 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -11.7) |
| [[SW480 (line)]] | alt | 33.1 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.325× (z -11.6) |
| [[BT-474 (line)]] | alt | 21.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 21.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 2 (1 ⚠) | — | [[Drospirenone (drug)]] 0.5 µM 0.0961× (z -10.5) |
| [[Hs 766T (line)]] | wt | 23.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 7.33 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +13.4) | — |
| [[PANC-1 (line)]] | alt | 28.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +15.0) | — |
| [[A-172 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 24.7 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0642× (z -9.0) |
| [[C-33 A (line)]] | alt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 9.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -9.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -11.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12462), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC4]] | +0.61 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[SLC35A4]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | +0.60 | +0.56 / +0.62 | both halves | 1e-05 | same gene group |
| [[TNFRSF12A]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[MTMR9]] | +0.58 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[UTP3]] | +0.58 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[FBXO38]] | +0.58 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[MRPL47]] | +0.57 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[GSS]] | +0.57 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[MPHOSPH6]] | +0.57 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[RFFL]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[ZBTB38]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IP4]] | -0.57 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[KMT5C]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[GIT1]] | -0.56 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.55 | -0.71 / -0.54 | both halves | 1e-05 |  |
| [[ELL3]] | -0.54 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[LAPTM4A]] | -0.53 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | -0.53 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[KDM3A]] | -0.53 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[MARCHF6]] | -0.53 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[RTN3]] | -0.52 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[RPA1]] | -0.52 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[SDHAP1]] | -0.52 | -0.71 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.547). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.9, 12.7); signed map (1.0, -31.0). **Vector** length 69.4, 12.5% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +10.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +12.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +5.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +1.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -3.1 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 81 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:47,836,902-48,002,561 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HFZ20; previously MRX45 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P51508](https://www.uniprot.org/uniprotkb/P51508) (Zinc finger protein 81):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [347344](https://www.ncbi.nlm.nih.gov/gene/347344):

> This gene encodes a protein that likely functions as a transcription factor. The protein contains an N-terminal KRAB domain and several C2H2-type zinc finger motifs. Mutations in this gene cause an X-linked form of intellectual disability (MRX45). Microduplication of a region of chromosome X including this gene has also been associated with other forms of intellectual disability. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:13156](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13156) · Entrez [347344](https://www.ncbi.nlm.nih.gov/gene/347344) · UniProt [P51508](https://www.uniprot.org/uniprotkb/P51508) · Ensembl [ENSG00000197779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197779)

## Data

Gene col 12462: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12462); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12462, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12462]; `tensor/DDL_lfc|DDL_z.npy` [12462]; `embed/gene_vectors.npy` [12462]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12462 or target_col == 12462). Every well: [[ZNF81 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF81.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
