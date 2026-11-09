---
symbol: "CKS1B"
type: "gene"
col: 10352
ensembl_id: "ENSG00000173207"
name: "CDC28 protein kinase regulatory subunit 1B"
location: "1q21.3"
module: 67
arm: "+"
pooled_cpm: 28.77
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CKS1B

*CDC28 protein kinase regulatory subunit 1B* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.22× (z +13.9, q 6e-41, up in 42 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +5.8, q 4e-07, up in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (A549 8.13×, NCI-H460 6.14×, A-172 5.49×, PANC-1 3.85×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-427 4.10×, NCI-H460 4.97×, LoVo 5.22×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 3.12×, SNU-423 3.80×).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.749× (z -3.9, q 0.046, down in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.225×, SW480 0.364×, KATO III 0.385×, HEC-1-A 0.411×, …); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.0790×, SNU-1 0.111×, H4 0.123×); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 2 lines (H4 0.0317×, A-172 0.234×; ⚠ cell-cycle shift, would explain all of this change); [[Saquinavir (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0613×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPC25]] (+0.78, fdr 7e-06), [[SPAG5]] (+0.76, fdr 7e-06), [[CDCA3]] (+0.76, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 12 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10352.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (A549 8.13×, NCI-H460 6.14×, A-172 5.49×, PANC-1 3.85×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-427 4.10×, NCI-H460 4.97×, LoVo 5.22×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 3.12×, SNU-423 3.80×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **4.22×** | +13.9 | 6e-41 | 42/43 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.97×** | +12.8 | 6e-35 | 37/37 (A-427, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.49×** | +8.1 | 7e-14 | 35/38 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **2.32×** | +8.1 | 8e-14 | 39/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **2.04×** | +6.6 | 4e-09 | 38/47 (A-172, LoVo, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.94×** | +6.4 | 1e-08 | 38/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.8 | 4e-07 | 30/47 (NCI-H2347, SNU-423, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~73% of this change | **1.77×** | +5.5 | 2e-06 | 34/46 (Panc 03.27, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.73×** | +5.1 | 2e-05 | 32/48 (NCI-H23, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.64×** | +4.8 | 1e-04 | 28/47 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.48×** | +3.8 | 0.008 | 24/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.47×** | +3.7 | 0.008 | 25/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +3.2 | 0.060 | 22/48 (NCI-H23, LoVo, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10352.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.225×, SW480 0.364×, KATO III 0.385×, HEC-1-A 0.411×, …); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (MIA PaCa-2 0.0790×, SNU-1 0.111×, H4 0.123×); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 2 lines (H4 0.0317×, A-172 0.234×; ⚠ cell-cycle shift, would explain all of this change); [[Saquinavir (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0613×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.749×** | -3.9 | 0.046 | 25/47 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.677×** | -3.7 | 0.046 | 25/48 (HCT15, A498, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.681×** | -3.7 | 0.046 | 24/47 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.673×** | -3.6 | 0.050 | 27/48 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.700× | -3.2 | 0.14 | 17/48 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |
| [[Tadalafil (drug)]] 5 µM |  | 0.709× | -3.2 | 0.15 | 19/47 (LOX-IMVI, NCI-H661, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.797× | -3.0 | 0.19 | 22/48 (A498, LS 180, …) | all doses, flat | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.80 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 31.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.49× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.234× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 54.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.10× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.9) |
| [[A498 (line)]] | wt | 45.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Selinexor (drug)]] 5 µM 0.360× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 24.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.13× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[H4 (line)]] | wt | 25.4 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0317× (z -14.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 25.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -8.8) |
| [[HOP62 (line)]] | alt | 26.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[J82 (line)]] | alt | 33.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LoVo (line)]] | wt | 14.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.22× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LOX-IMVI (line)]] | wt | 15.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.51× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H460 (line)]] | wt | 25.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[PANC-1 (line)]] | alt | 42.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SW480 (line)]] | alt | 29.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.5) |
| [[C32 (line)]] | wt | 15.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.66× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[CFPAC-1 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HT-29 (line)]] | alt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -8.6) |
| [[KATO III (line)]] | alt | 32.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -9.4) |
| [[LS 180 (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.288× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0790× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 64.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H2347 (line)]] | alt | 42.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 20.3 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0613× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SNU-1 (line)]] | wt | 21.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -8.9) |
| [[SNU-423 (line)]] | alt | 16.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 31.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[AN3 CA (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPC25]] | +0.78 | +0.80 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[SPAG5]] | +0.76 | +0.80 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CDCA3]] | +0.76 | +0.79 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 514 |
| [[NUSAP1]] | +0.76 | +0.68 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 603 |
| [[KIF22]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[TICRR]] | +0.75 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[PBK]] | +0.75 | +0.79 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 537 |
| [[SHCBP1]] | +0.74 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[CENPN]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 | STRING 506 |
| [[RAD51AP1]] | +0.74 | +0.75 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 465 |
| [[MAD2L1]] | +0.74 | +0.80 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 722 |
| [[OIP5]] | +0.73 | +0.76 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises CKS1B's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.79× lower at baseline in the lines without PIMREG | 0.090 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CKS1B's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without AURKB | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.6, -52.7); signed map (-45.9, -42.2). **Vector** length 86.5, 24.7% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.64 to 8); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.63 to 4); *Nucleosome assembly* (reactome, mean cos +0.63 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +3.5 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +3.5 | +4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +3.3 | +8.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +3.1 | +3.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +0.4 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +1.3 | -0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.3 | +2.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.3 | +1.6 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.5 | -3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.4 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -0.1 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | +0.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | CDC28 protein kinase regulatory subunit 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,974,653-154,979,251 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ckshs1, CKS1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 10 pathways, smallest: Cyclin D associated events in G1; G1 Phase; SCF(Skp2)-mediated degradation of p27/p21 |
| Matched by | ensembl_id |

**Function**, from UniProt [P61024](https://www.uniprot.org/uniprotkb/P61024) (Cyclin-dependent kinases regulatory subunit 1):

> Component of the substrate-specific subunit in cullin-RING E3 ubiquitin-protein ligase complexes. The E3 ubiquitin-protein ligase activity is regulated by the COP9 signalosome (CSN), which restores the ligase to its inactive state and resets the ligase for substrate recognition by reversing the activating neddylation on the cullin. Binds to the catalytic subunit of the cyclin dependent kinases and is essential for their biological function.

**Summary**, from NCBI Gene [1163](https://www.ncbi.nlm.nih.gov/gene/1163):

> CKS1B protein binds to the catalytic subunit of the cyclin dependent kinases and is essential for their biological function. The CKS1B mRNA is found to be expressed in different patterns through the cell cycle in HeLa cells, which reflects a specialized role for the encoded protein. At least two transcript variants have been identified for this gene, and it appears that only one of them encodes a protein. [provided by RefSeq, Sep 2008]

**Accessions** — [HGNC:19083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19083) · Entrez [1163](https://www.ncbi.nlm.nih.gov/gene/1163) · UniProt [P61024](https://www.uniprot.org/uniprotkb/P61024) · Ensembl [ENSG00000173207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173207)

## Data

Gene col 10352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10352); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10352]; `tensor/DDL_lfc|DDL_z.npy` [10352]; `embed/gene_vectors.npy` [10352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10352 or target_col == 10352). Every well: [[CKS1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CKS1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
