---
symbol: "ENO1"
type: "gene"
col: 1092
ensembl_id: "ENSG00000074800"
name: "enolase 1"
location: "1p36.23"
module: 99
arm: "+"
pooled_cpm: 739.92
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# ENO1

*enolase 1* — 1p36.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.96× (z +8.3, q 7e-14, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.36× (z +3.8, q 0.019, up in 41 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A498 5.04×, A549 4.39×, PANC-1 3.68×, NCI-H460 3.47×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (A498 4.99×, A549 4.05×, PANC-1 3.44×, NCI-H460 3.25×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 2.75×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.464× (z -13.2, q 5e-37, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LDHA]] (+0.82, fdr 7e-06), [[PGK1]] (+0.79, fdr 7e-06), [[PKM]] (+0.65, fdr 7e-06); moves opposite to [[TMEM267]] (-0.48, fdr 1e-04), [[PTPN9]] (-0.48, fdr 5e-04), [[CCZ1P1]] (-0.48, fdr 4e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1092.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A498 5.04×, A549 4.39×, PANC-1 3.68×, NCI-H460 3.47×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (A498 4.99×, A549 4.05×, PANC-1 3.44×, NCI-H460 3.25×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 2.75×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.96×** | +8.3 | 7e-14 | 47/49 (A498, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.92×** | +7.7 | 4e-12 | 41/44 (A498, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~88% of this change | **1.40×** | +4.1 | 0.007 | 41/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.43×** | +4.0 | 0.009 | 33/45 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.019 | 41/48 (MIA PaCa-2, AsPC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.34×** | +3.6 | 0.029 | 31/48 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.31×** | +3.3 | 0.073 | 42/48 (Panc 03.27, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.073 | 31/48 (MIA PaCa-2, A549, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.20×** | +3.2 | 0.083 | 23/48 (PANC-1, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1092.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.464×** | -13.2 | 5e-37 | 46/48 (HCT15, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.537×** | -10.7 | 3e-24 | 40/49 (HCT15, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.602×** | -6.0 | 4e-07 | 37/47 (HCT15, COLO 205, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.732×** | -5.4 | 1e-05 | 39/48 (RKO, C32, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **0.683×** | -4.7 | 4e-04 | 41/48 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.693×** | -4.5 | 7e-04 | 43/48 (RKO, C32, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.508×** | -4.3 | 0.001 | 45/49 (HCT15, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.711×** | -4.2 | 0.002 | 29/48 (C-33 A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.711×** | -4.2 | 0.002 | 40/48 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -3.9 | 0.004 | 35/48 (C32, C-33 A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.745×** | -3.6 | 0.017 | 42/49 (J82, BT-474, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.754×** | -3.4 | 0.026 | 34/48 (BT-474, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.757×** | -3.4 | 0.028 | 40/48 (RKO, A-172, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.822×** | -3.3 | 0.035 | 26/48 (AN3 CA, SNU-1, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.613×** | -3.1 | 0.066 | 43/49 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.769×** | -3.1 | 0.071 | 29/48 (C-33 A, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1092. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 1,252 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -15.4) |
| [[NCI-H460 (line)]] | wt | 651 | 5 (5 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -10.8) |
| [[HCT15 (line)]] | alt | 1,228 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -24.1) |
| [[MIA PaCa-2 (line)]] | alt | 796 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -21.0) |
| [[RKO (line)]] | wt | 800 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -16.5) |
| [[C-33 A (line)]] | alt | 644 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -20.9) |
| [[HT-29 (line)]] | alt | 575 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 636 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -11.6) |
| [[SW480 (line)]] | alt | 858 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -20.7) |
| [[A498 (line)]] | wt | 282 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A549 (line)]] | wt | 531 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[H4 (line)]] | wt | 905 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -11.8) |
| [[KATO III (line)]] | alt | 549 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 539 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -9.1) |
| [[PANC-1 (line)]] | alt | 743 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SHP-77 (line)]] | alt | 1,082 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -19.4) |
| [[SNU-1 (line)]] | wt | 729 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -22.8) |
| [[BT-474 (line)]] | alt | 544 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -13.5) |
| [[COLO 205 (line)]] | alt | 540 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 957 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -10.1) |
| [[HOP62 (line)]] | alt | 1,169 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -13.5) |
| [[Hs 766T (line)]] | wt | 1,055 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -14.0) |
| [[LoVo (line)]] | wt | 534 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -9.4) |
| [[LS 180 (line)]] | wt | 750 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 539 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H23 (line)]] | alt | 601 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 923 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -15.6) |
| [[SNU-423 (line)]] | alt | 783 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW 900 (line)]] | alt | 616 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -14.6) |
| [[A-172 (line)]] | wt | 502 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 542 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.8) |
| [[AN3 CA (line)]] | alt | 769 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 1,016 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -10.7) |
| [[CHP-212 (line)]] | wt | 423 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -16.6) |
| [[HepG2_C3A (line)]] | wt | 1,657 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -17.1) |
| [[HS-578T (line)]] | alt | 1,249 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 752 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -9.0) |
| [[J82 (line)]] | alt | 1,095 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 809 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 832 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -15.1) |
| [[NCI-H661 (line)]] | alt | 515 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 419 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 809 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -13.7) |
| [[SW 1088 (line)]] | alt | 1,092 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -8.5) |
| [[SW 1271 (line)]] | alt | 630 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.1) |
| [[SW48 (line)]] | wt | 563 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 389 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 608 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 733 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 238 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1092), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDHA]] | +0.82 | +0.85 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 924 |
| [[PGK1]] | +0.79 | +0.77 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 996 |
| [[PKM]] | +0.65 | +0.72 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 997 |
| [[ALDOA]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 988 |
| [[GBE1]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 500 |
| [[PLOD2]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[USP9X]] | +0.60 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[POLR2E]] | +0.59 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[PFKFB3]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 | same gene group; pathway: HALLMARK_HYPOXIA; STRING 682 |
| [[BNIP3]] | +0.57 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[CLTC]] | +0.55 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[PFKP]] | +0.53 | +0.46 / +0.59 | both halves | 3e-05 | pathway: HALLMARK_GLYCOLYSIS; STRING 892 |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM267]] | -0.48 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[PTPN9]] | -0.48 | -0.23 / -0.43 | both halves | 5e-04 |  |
| [[CCZ1P1]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[POMZP3]] | -0.48 | -0.24 / -0.51 | both halves | 5e-04 |  |
| [[SNHG12]] | -0.47 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[GPAT4-AS1]] | -0.47 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[ZBTB8A]] | -0.47 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[RNF135]] | -0.47 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[PPP1R26-AS1]] | -0.47 | -0.35 / -0.32 | both halves | 2e-04 |  |
| [[SLC12A9]] | -0.47 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[PLPP5]] | -0.46 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[MORN4]] | -0.46 | -0.37 / -0.52 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ENO1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PFKP]] | C | PFKP activity raises ENO1's level | lines that do not express PFKP (3) vs lines expressing it (47) | 1.58× lower at baseline in the lines without PFKP | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.2, 22.4); signed map (-37.2, 29.2). **Vector** length 123, 57.7% of its response variance represented; |z| ≥ 3 in 1,077 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.54 to 7); *Regulation of pyruvate metabolism* (reactome, mean cos +0.55 to 4); *Pyruvate metabolism* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +1.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +6.1 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.6 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | -0.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -8.5 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -6.5 | -4.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -5.4 | -5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -10.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.9 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -0.0 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -3.2 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.0 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -0.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | enolase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.23 — chr1:8,861,000-8,879,190 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PPH, MBP-1; previously ENO1L1, MPB1, ENO1-IT1 |
| Gene groups (HGNC) | Enolases; MicroRNA protein coding host genes |
| Hallmark sets | GLYCOLYSIS, HYPOXIA, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: Gluconeogenesis; Response of Mtb to phagocytosis; Infection with Mycobacterium tuberculosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P06733](https://www.uniprot.org/uniprotkb/P06733) (Alpha-enolase):

> Enolase that catalyzes the conversion of 2-phosphoglycerate to phosphoenolpyruvate in glycolysis and the reverse reaction in gluconeogenesis. Also involved in various processes such as growth control, hypoxia tolerance and allergic responses. May also function in the intravascular and pericellular fibrinolytic system due to its ability to serve as a receptor and activator of plasminogen on the cell surface of several cell-types such as leukocytes and neurons. Stimulates immunoglobulin …

**Summary**, from NCBI Gene [2023](https://www.ncbi.nlm.nih.gov/gene/2023):

> This gene encodes alpha-enolase, one of three enolase isoenzymes found in mammals. Each isoenzyme is a homodimer composed of 2 alpha, 2 gamma, or 2 beta subunits, and functions as a glycolytic enzyme. Alpha-enolase in addition, functions as a structural lens protein (tau-crystallin) in the monomeric form. Alternative splicing of this gene results in a shorter isoform that has been shown to bind to the c-myc promoter and function as a tumor suppressor. Several pseudogenes have been identified, …

**Accessions** — [HGNC:3350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3350) · Entrez [2023](https://www.ncbi.nlm.nih.gov/gene/2023) · UniProt [P06733](https://www.uniprot.org/uniprotkb/P06733) · Ensembl [ENSG00000074800](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074800)

## Data

Gene col 1092: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1092); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1092, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1092]; `tensor/DDL_lfc|DDL_z.npy` [1092]; `embed/gene_vectors.npy` [1092]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1092 or target_col == 1092). Every well: [[ENO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
