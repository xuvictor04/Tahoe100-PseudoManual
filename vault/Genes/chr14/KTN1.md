---
symbol: "KTN1"
type: "gene"
col: 4763
ensembl_id: "ENSG00000126777"
name: "kinectin 1"
location: "14q22.3"
module: 179
arm: "-"
pooled_cpm: 585.97
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# KTN1

*kinectin 1* — 14q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.93× (z +11.7, q 5e-29, up in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.29× (z +4.7, q 1e-04, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.664× (z -7.3, q 2e-10, down in 37 of 47 measured lines) ⚠ toxic. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H1792 0.491×, A549 0.536×, C-33 A 0.574×, MIA PaCa-2 0.635×; ⚠ cell-cycle shift, explains ~25% of this change); [[Selinexor (drug)]] 5 µM in 1 line (C32 0.570×; ⚠ cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.378×; ⚠ cell-cycle shift, explains ~25% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FER]] (+0.58, fdr 1e-05), [[EEA1]] (+0.58, fdr 7e-06), [[CAST]] (+0.55, fdr 1e-04); moves opposite to [[SNHG21]] (-0.54, fdr 1e-05), [[ZNF749]] (-0.54, fdr 3e-05), [[ZNF384]] (-0.53, fdr 3e-05).
> It sits in the **-** arm of [[Module 179]] (RHOA GTPase cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4763.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +11.7 | 5e-29 | 42/44 (A498, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +10.9 | 5e-25 | 47/49 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.50×** | +10.7 | 3e-24 | 39/48 (SNU-1, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.49×** | +7.2 | 9e-11 | 41/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.46×** | +7.0 | 2e-10 | 39/48 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +6.2 | 5e-08 | 30/45 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.40×** | +6.0 | 1e-07 | 36/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.35×** | +5.6 | 1e-06 | 33/48 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.34×** | +5.4 | 4e-06 | 36/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 1e-04 | 34/48 (NCI-H2030, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +4.6 | 2e-04 | 29/48 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +4.3 | 7e-04 | 29/48 (SW1417, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.29×** | +4.2 | 0.001 | 29/48 (A-172, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.22×** | +3.6 | 0.011 | 24/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.035 | 24/48 (CFPAC-1, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4763.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H1792 0.491×, A549 0.536×, C-33 A 0.574×, MIA PaCa-2 0.635×; ⚠ cell-cycle shift, explains ~25% of this change); [[Selinexor (drug)]] 5 µM in 1 line (C32 0.570×; ⚠ cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.378×; ⚠ cell-cycle shift, explains ~25% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.664×** | -7.3 | 2e-10 | 37/47 (Panc 03.27, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.713×** | -5.5 | 1e-05 | 42/48 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.842× | -4.5 | 0.001 | 19/48 (C32, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Folic acid (drug)]] 5 µM |  | 0.882× | -3.2 | 0.13 | 1/48 (CHP-212) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -3.2 | 0.13 | 0/50 | inconsistent across doses |  |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.840× | -3.2 | 0.15 | 17/48 (SNU-1, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4763. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 1,070 | 6 (6 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +13.6) ⚠ cell-cycle shift, explains ~37% of this change | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.378× (z -11.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 616 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.4) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[PANC-1 (line)]] | alt | 704 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +12.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 455 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +13.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 689 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +9.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -15.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW1417 (line)]] | alt | 494 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +15.8) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[A549 (line)]] | wt | 647 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.47× (z +12.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -12.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[KATO III (line)]] | alt | 405 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +14.0) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[LoVo (line)]] | wt | 650 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.0) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[NCI-H2030 (line)]] | alt | 1,029 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.59× (z +9.0) | — |
| [[A-172 (line)]] | wt | 262 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.2) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[A-427 (line)]] | wt | 464 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +11.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 652 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +17.4) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[CFPAC-1 (line)]] | alt | 626 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +12.7) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[H4 (line)]] | wt | 501 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +14.5) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[HOP62 (line)]] | alt | 584 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.2) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[HT-29 (line)]] | alt | 316 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.5) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[NCI-H460 (line)]] | wt | 511 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +11.1) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[SNU-1 (line)]] | wt | 368 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +17.9) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[SNU-423 (line)]] | alt | 463 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +11.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 412 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.50× (z +13.2) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 474 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.5) ⚠ cell-cycle shift, explains ~69% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.492× (z -8.7) ⚠ cell-cycle shift, explains ~96% of this change |
| [[C32 (line)]] | wt | 632 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.5) ⚠ cell-cycle shift, explains ~69% of this change | [[Selinexor (drug)]] 5 µM 0.570× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 266 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.9) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[Hs 766T (line)]] | wt | 710 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +8.7) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[HS-578T (line)]] | alt | 406 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +11.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 614 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.99× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 545 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.03× (z +10.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 375 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 629 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.37× (z +13.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 504 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +10.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 796 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -10.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HCT15 (line)]] | alt | 738 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.3) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 560 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 1,355 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.93× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 506 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.50× (z +9.1) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[Panc 03.27 (line)]] | alt | 714 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.571× (z -9.0) ⚠ toxic |
| [[SW 900 (line)]] | alt | 560 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +10.3) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[CHP-212 (line)]] | wt | 471 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 463 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 543 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 705 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 543 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 547 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 499 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 573 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 536 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 415 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 591 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 620 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4763), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FER]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[EEA1]] | +0.58 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[CAST]] | +0.55 | +0.33 / +0.61 | both halves | 1e-04 |  |
| [[ANKRD12]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[DNAJC21]] | +0.54 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[PRRC2C]] | +0.53 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ROCK1]] | +0.53 | +0.34 / +0.57 | both halves | 1e-04 | pathway: RHO GTPase Effectors |
| [[ROCK2]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[SPAG9]] | +0.52 | +0.32 / +0.55 | both halves | 2e-04 |  |
| [[ATRX]] | +0.52 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[GKAP1]] | +0.52 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[DST]] | +0.52 | +0.55 / +0.52 | both halves | 1e-05 | pathway: RND2 GTPase cycle |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG21]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ZNF749]] | -0.54 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[ZNF384]] | -0.53 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[RBM14]] | -0.53 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[SMPD4]] | -0.51 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[NIF3L1]] | -0.51 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[KANSL2]] | -0.51 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[THOC3]] | -0.51 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[SPATA2]] | -0.50 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[SNRPG]] | -0.50 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[DIDO1]] | -0.50 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[RNF139]] | -0.50 | -0.35 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **-** arm (projection on the module's main direction -0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-1.2, -18.1); signed map (10.5, -10.3). **Vector** length 121, 49.7% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +7.4 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.4 | +7.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.8 | +7.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +0.3 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +2.8 | +1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.5 | +1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -14.0 | -7.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.3 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -7.6 | -5.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.6 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.5 | -1.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.8 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.1 | -1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | kinectin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.3 — chr14:55,559,072-55,701,526 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0004, CG1, KNT |
| Reactome | 13 pathways, smallest: RHO GTPases activate KTN1; RND2 GTPase cycle; RND3 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UP2](https://www.uniprot.org/uniprotkb/Q86UP2) (Kinectin):

> Receptor for kinesin thus involved in kinesin-driven vesicle motility. Accumulates in integrin-based adhesion complexes (IAC) upon integrin aggregation by fibronectin.

**Summary**, from NCBI Gene [3895](https://www.ncbi.nlm.nih.gov/gene/3895):

> This gene encodes an integral membrane protein that is a member of the kinectin protein family. The encoded protein is primarily localized to the endoplasmic reticulum membrane. This protein binds kinesin and may be involved in intracellular organelle motility. This protein also binds translation elongation factor-delta and may be involved in the assembly of the elongation factor-1 complex. Alternate splicing results in multiple transcript variants of this gene. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:6467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6467) · Entrez [3895](https://www.ncbi.nlm.nih.gov/gene/3895) · UniProt [Q86UP2](https://www.uniprot.org/uniprotkb/Q86UP2) · Ensembl [ENSG00000126777](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126777)

## Data

Gene col 4763: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4763); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4763, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4763]; `tensor/DDL_lfc|DDL_z.npy` [4763]; `embed/gene_vectors.npy` [4763]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4763 or target_col == 4763). Every well: [[KTN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KTN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
