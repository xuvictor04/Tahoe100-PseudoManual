---
symbol: "CHM"
type: "gene"
col: 12011
ensembl_id: "ENSG00000188419"
name: "CHM Rab escort protein"
location: "Xq21.2"
module: 28
arm: "+"
pooled_cpm: 82.18
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# CHM

*CHM Rab escort protein* — Xq21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.34× (z +6.9, q 4e-09, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (13 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.603× (z -8.4, q 2e-14, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.822× (z -4.6, q 2e-04, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW48 0.0612×, A-427 0.246×, SK-MEL-2 0.308×, C-33 A 0.276×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 0.251×, H4 0.192×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 0.350×, LS 180 0.302×; ⚠ cell-cycle shift, would explain all of this change); [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H596 0.124×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GATB]] (+0.71, fdr 7e-06), [[GTF2H1]] (+0.69, fdr 7e-06), [[FCF1]] (+0.69, fdr 1e-05); moves opposite to [[PDXP]] (-0.66, fdr 1e-05), [[LRP5L]] (-0.62, fdr 1e-05), [[NR2F6]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12011.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +6.9 | 4e-09 | 32/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.6 | 0.001 | 28/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.20×** | +4.3 | 0.004 | 22/48 (Hs 766T, HT-29, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.038 | 24/50 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 1.46× | +3.3 | 0.11 | 23/49 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 1.45× | +3.2 | 0.12 | 22/49 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 1.44× | +3.2 | 0.12 | 14/48 (NCI-H460, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.24× | +3.0 | 0.16 | 17/50 (NCI-H460, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12011.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW48 0.0612×, A-427 0.246×, SK-MEL-2 0.308×, C-33 A 0.276×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 0.251×, H4 0.192×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 0.350×, LS 180 0.302×; ⚠ cell-cycle shift, would explain all of this change); [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H596 0.124×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.603×** | -8.4 | 2e-14 | 42/48 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.594×** | -8.3 | 2e-14 | 42/47 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.606×** | -8.3 | 2e-14 | 37/48 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.608×** | -8.3 | 2e-14 | 38/48 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.627×** | -7.5 | 8e-12 | 37/47 (H4, LS 180, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.662×** | -6.9 | 7e-10 | 32/48 (SW480, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.777×** | -5.9 | 3e-07 | 28/49 (A549, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.728×** | -5.3 | 9e-06 | 32/48 (AsPC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.715×** | -5.1 | 2e-05 | 26/45 (NCI-H1573, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.747×** | -4.8 | 7e-05 | 30/49 (SW48, A-427, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.822×** | -4.6 | 2e-04 | 22/48 (HOP62, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | **0.752×** | -4.6 | 2e-04 | 25/44 (A-427, KATO III, …) | all doses, flat | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.815×** | -3.4 | 0.030 | 22/48 (RKO, SNU-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.819×** | -3.3 | 0.036 | 20/48 (J82, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.822×** | -3.3 | 0.042 | 21/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12011. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 126 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.251× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[AsPC-1 (line)]] | alt | 98.0 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 101 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.368× (z -9.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[H4 (line)]] | wt | 91.9 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H1573 (line)]] | alt | 105 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +16.0) | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[SNU-423 (line)]] | alt | 182 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.425× (z -9.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LS 180 (line)]] | wt | 47.0 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 99.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +18.6) | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[A-427 (line)]] | wt | 73.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -21.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[C-33 A (line)]] | alt | 96.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 82.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.452× (z -9.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[Hs 766T (line)]] | wt | 128 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.448× (z -8.6) ⚠ toxic |
| [[KATO III (line)]] | alt | 79.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[LOX-IMVI (line)]] | wt | 90.7 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 113 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.420× (z -9.2) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 111 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.476× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H596 (line)]] | alt | 86.3 | 0 | 2 (1 ⚠) | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.124× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 82.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -9.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SK-MEL-2 (line)]] | alt | 115 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 63.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0612× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.361× (z -9.7) ⚠ toxic |
| [[A498 (line)]] | wt | 68.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +9.4) | — |
| [[A549 (line)]] | wt | 74.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -10.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 95.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 76.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +12.3) | — |
| [[HepG2_C3A (line)]] | wt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 79.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 75.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 89.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.501× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[RKO (line)]] | wt | 92.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 1088 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0753× (z -10.2) ⚠ cell-cycle shift, explains ~90% of this change |
| [[AN3 CA (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12011), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATB]] | +0.71 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[GTF2H1]] | +0.69 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[FCF1]] | +0.69 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[USP40]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[RIMOC1]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MRPL45]] | +0.65 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[AIMP1]] | +0.64 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[DNAJC8]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[METTL6]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[DARS1]] | +0.62 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[STAMBP]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[TRMT13]] | +0.61 | +0.58 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDXP]] | -0.66 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[LRP5L]] | -0.62 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[NR2F6]] | -0.60 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[UBTD1]] | -0.59 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[CYTH3]] | -0.59 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[SGPP1]] | -0.58 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.57 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[FOXK2]] | -0.57 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[GLRX5]] | -0.57 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[UBE2G1]] | -0.56 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[C2CD2L]] | -0.56 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[ABHD12]] | -0.56 | -0.58 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.536). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.2, 8.5); signed map (10.1, -23.8). **Vector** length 101, 29.1% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +4.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +4.9 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.9 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +1.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.5 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +1.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.9 | -8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -4.4 | -8.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -2.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.1 | -8.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | CHM Rab escort protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.2 — chrX:85,861,180-86,047,561 (-) |
| Ensembl biotype | protein_coding |
| Also known as | REP-1; previously TCD, DXS540 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Rab geranylgeranyltransferase subunits |
| Reactome | 8 pathways, smallest: TP53 regulates transcription of several additional cell death genes whose specific roles in p53-dependent apoptosis remain uncertain; TP53 Regulates Transcription of Cell Death Genes; RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P24386](https://www.uniprot.org/uniprotkb/P24386) (Rab proteins geranylgeranyltransferase component A 1):

> Substrate-binding subunit of the Rab geranylgeranyltransferase (GGTase) complex. Binds unprenylated Rab proteins and presents the substrate peptide to the catalytic component B composed of RABGGTA and RABGGTB, and remains bound to it after the geranylgeranyl transfer reaction. The component A is thought to be regenerated by transferring its prenylated Rab back to the donor membrane. Besides, a pre-formed complex consisting of CHM and the Rab GGTase dimer (RGGT or component B) can bind to and …

**Summary**, from NCBI Gene [1121](https://www.ncbi.nlm.nih.gov/gene/1121):

> This gene encodes component A of the RAB geranylgeranyl transferase holoenzyme. In the dimeric holoenzyme, this subunit binds unprenylated Rab GTPases and then presents them to the catalytic Rab GGTase subunit for the geranylgeranyl transfer reaction. Rab GTPases need to be geranylgeranyled on either one or two cysteine residues in their C-terminus to localize to the correct intracellular membrane. Mutations in this gene are a cause of choroideremia; also known as tapetochoroidal dystrophy …

**Accessions** — [HGNC:1940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1940) · Entrez [1121](https://www.ncbi.nlm.nih.gov/gene/1121) · UniProt [P24386](https://www.uniprot.org/uniprotkb/P24386) · Ensembl [ENSG00000188419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188419)

## Data

Gene col 12011: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12011); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12011, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12011]; `tensor/DDL_lfc|DDL_z.npy` [12011]; `embed/gene_vectors.npy` [12011]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12011 or target_col == 12011). Every well: [[CHM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
