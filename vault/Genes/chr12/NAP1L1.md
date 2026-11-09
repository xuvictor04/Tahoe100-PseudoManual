---
symbol: "NAP1L1"
type: "gene"
col: 11888
ensembl_id: "ENSG00000187109"
name: "nucleosome assembly protein 1 like 1"
location: "12q21.1"
module: 43
arm: "+"
pooled_cpm: 593.23
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# NAP1L1

*nucleosome assembly protein 1 like 1* — 12q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.33× (z +11.1, q 1e-25, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +5.6, q 2e-06, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.674× (z -5.2, q 1e-04, down in 38 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (RKO 0.480×, LS 180 0.414×, SW48 0.449×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (RKO 0.523×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPM1]] (+0.65, fdr 1e-05), [[RPS4X]] (+0.62, fdr 1e-05), [[RPS12]] (+0.61, fdr 8e-06); moves opposite to [[RANBP6]] (-0.58, fdr 3e-05), [[SLC39A3]] (-0.58, fdr 3e-05), [[PRPF4]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +11.1 | 1e-25 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +8.2 | 8e-14 | 42/43 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +7.3 | 5e-11 | 44/46 (COLO 205, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.74×** | +7.3 | 5e-11 | 42/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +6.9 | 5e-10 | 43/44 (HT-29, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +6.8 | 1e-09 | 42/47 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.6 | 2e-06 | 43/49 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.1 | 3e-05 | 33/48 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +4.9 | 5e-05 | 42/47 (RPMI-7951, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.9 | 5e-05 | 37/47 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 4e-04 | 39/47 (C32, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.24×** | +3.9 | 0.005 | 24/47 (C32, CFPAC-1, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.33×** | +3.7 | 0.008 | 34/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.31×** | +3.5 | 0.017 | 35/47 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.022 | 35/47 (HT-29, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.2 | 0.048 | 22/47 (CFPAC-1, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11888.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (RKO 0.480×, LS 180 0.414×, SW48 0.449×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (RKO 0.523×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.674×** | -5.2 | 1e-04 | 38/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.731×** | -4.1 | 0.011 | 33/47 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 904 | 7 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.48× (z +12.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 380 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +8.7) | — |
| [[LoVo (line)]] | wt | 717 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +13.3) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 451 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 562 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.8) | — |
| [[RKO (line)]] | wt | 794 | 2 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.480× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.523× (z -8.9) |
| [[A498 (line)]] | wt | 664 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +10.4) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 601 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +8.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 684 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.30× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 528 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +13.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 641 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 766 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +11.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 401 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 283 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 265 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.26× (z +11.4) ⚠ toxic | — |
| [[HCT15 (line)]] | alt | 442 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 698 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 518 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 574 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 454 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 374 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +12.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 531 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 459 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.414× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 885 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 662 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +9.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW48 (line)]] | wt | 555 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.449× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 1,141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +11.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 705 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +9.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 638 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 411 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +8.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 575 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.23× (z +8.9) ⚠ toxic | — |
| [[NCI-H2030 (line)]] | alt | 633 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 804 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 527 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +16.3) | — |
| [[Panc 03.27 (line)]] | alt | 372 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +11.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 809 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 423 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 702 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 200 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 294 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 624 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1,137 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 448 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 634 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 637 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 496 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 798 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 398 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 778 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 12 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPM1]] | +0.65 | +0.57 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 827 |
| [[RPS4X]] | +0.62 | +0.56 / +0.68 | both halves | 1e-05 | STRING 458 |
| [[RPS12]] | +0.61 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[RPL21]] ⚠ | +0.60 | +0.48 / +0.69 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS6]] ⚠ | +0.60 | +0.52 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 704; ⚠ in the vector space only through flagged drug-doses |
| [[RPS20]] | +0.58 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[RPS2]] | +0.58 | +0.51 / +0.74 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[NACA]] ⚠ | +0.56 | +0.47 / +0.60 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | +0.56 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[RPL37A]] ⚠ | +0.56 | +0.49 / +0.65 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL13A]] | +0.56 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[RPL30]] ⚠ | +0.55 | +0.48 / +0.60 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL14]] | +0.54 | +0.49 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[RPL7]] | +0.54 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[EEF1B2]] | +0.53 | +0.38 / +0.59 | both halves | 6e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 466 |
| [[RPL5]] | +0.53 | +0.48 / +0.67 | both halves | 2e-05 | STRING 596 |
| [[HINT1]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANBP6]] | -0.58 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[SLC39A3]] | -0.58 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[PRPF4]] | -0.56 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[RNF40]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[POP4]] | -0.56 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[MRPL28]] | -0.56 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[RAB8A]] | -0.55 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[TIMM22]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[EIF2B2]] | -0.55 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[EXOC8]] | -0.54 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[ZKSCAN2]] | -0.54 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[MUL1]] | -0.54 | -0.56 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NAP1L1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.528). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-44.5, -29.5); signed map (-59.7, -6.3). **Vector** length 105, 48.1% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.0 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.5 | +1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | -0.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.5 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.9 | -0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.0 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.1 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | nucleosome assembly protein 1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.1 — chr12:76,036,585-76,084,735 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NRP, NAP1, NAP1L, MGC8688, MGC23410 |
| Gene groups (HGNC) | Nucleosome assembly protein 1 like family |
| Hallmark sets | E2F_TARGETS, MYC_TARGETS_V1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P55209](https://www.uniprot.org/uniprotkb/P55209) (Nucleosome assembly protein 1-like 1):

> Histone chaperone that plays a role in the nuclear import of H2A-H2B and nucleosome assembly. Also participates in several important DNA repair mechanisms: greatly enhances ERCC6-mediated chromatin remodeling which is essential for transcription-coupled nucleotide excision DNA repair. Also stimulates homologous recombination (HR) by RAD51 and RAD54 which is essential in mitotic DNA double strand break (DSB) repair. Plays a key role in the regulation of embryonic neurogenesis (By similarity). …

**Summary**, from NCBI Gene [4673](https://www.ncbi.nlm.nih.gov/gene/4673):

> This gene encodes a member of the nucleosome assembly protein (NAP) family. This protein participates in DNA replication and may play a role in modulating chromatin formation and contribute to the regulation of cell proliferation. Alternative splicing results in multiple transcript variants encoding different isoforms; however, not all have been fully described. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:7637](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7637) · Entrez [4673](https://www.ncbi.nlm.nih.gov/gene/4673) · UniProt [P55209](https://www.uniprot.org/uniprotkb/P55209) · Ensembl [ENSG00000187109](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187109)

## Data

Gene col 11888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11888); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11888]; `tensor/DDL_lfc|DDL_z.npy` [11888]; `embed/gene_vectors.npy` [11888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11888 or target_col == 11888). Every well: [[NAP1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAP1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
