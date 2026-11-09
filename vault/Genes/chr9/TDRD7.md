---
symbol: "TDRD7"
type: "gene"
col: 12132
ensembl_id: "ENSG00000196116"
name: "tudor domain containing 7"
location: "9q22.33"
module: 32
arm: "+"
pooled_cpm: 71.36
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 41
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 64
direction_downstream: 15
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# TDRD7

*tudor domain containing 7* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.44× (z +4.7, q 0.002, up in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 2.94×, LS 180 2.11×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 3.17×; ⚠ cell-cycle shift, would explain all of this change); [[TAK-901 (drug)]] 5 µM in 1 line (NCI-H460 6.92×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (22 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.333× (z -14.0, q 5e-42, down in 33 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.419× (z -11.5, q 2e-28, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMPK2]] (+0.85, fdr 7e-06), [[USP18]] (+0.84, fdr 7e-06), [[MX1]] (+0.83, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 64 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 15 go from it, the strongest it → [[PARP10]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12132.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 2.94×, LS 180 2.11×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 3.17×; ⚠ cell-cycle shift, would explain all of this change); [[TAK-901 (drug)]] 5 µM in 1 line (NCI-H460 6.92×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +4.7 | 0.002 | 25/47 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.067 | 22/48 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.31× | +3.3 | 0.18 | 20/47 (AsPC-1, J82, …) | rises with dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.28 | 12/49 (SW1417, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 23 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12132.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.333×** | -14.0 | 5e-42 | 33/41 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.419×** | -11.5 | 2e-28 | 45/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.405×** | -11.1 | 4e-26 | 40/49 (A-172, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.466×** | -10.1 | 5e-22 | 42/47 (NCI-H1573, A549, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.614×** | -9.1 | 7e-18 | 32/49 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.522×** | -8.6 | 6e-16 | 36/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.558×** | -7.7 | 8e-13 | 34/49 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.552×** | -7.6 | 3e-12 | 34/47 (HepG2/C3A, RKO, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.546×** | -7.4 | 7e-12 | 34/42 (A-172, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.678×** | -7.3 | 2e-11 | 30/49 (MIA PaCa-2, C-33 A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -7.1 | 5e-11 | 39/49 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.702×** | -6.6 | 2e-09 | 26/48 (MIA PaCa-2, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.599×** | -6.4 | 7e-09 | 32/48 (MIA PaCa-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.623×** | -6.3 | 2e-08 | 31/49 (C-33 A, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.629×** | -6.1 | 3e-08 | 32/48 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.515×** | -4.6 | 1e-04 | 25/48 (A-172, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.725×** | -4.2 | 5e-04 | 25/48 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.734×** | -4.1 | 0.001 | 28/48 (SNU-423, HS-578T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.739×** | -4.0 | 0.001 | 27/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.614×** | -3.4 | 0.012 | 19/48 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.778×** | -3.3 | 0.015 | 16/48 (SNU-423, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 201 | 0 | 19 (15 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -17.4) |
| [[MIA PaCa-2 (line)]] | alt | 81.9 | 0 | 16 (8 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0964× (z -16.2) |
| [[A-172 (line)]] | wt | 214 | 0 | 15 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0945× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.159× (z -17.8) |
| [[SNU-423 (line)]] | alt | 111 | 0 | 13 (9 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.160× (z -14.2) |
| [[RKO (line)]] | wt | 139 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0791× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.302× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 71.1 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -11.0) |
| [[HS-578T (line)]] | alt | 76.3 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 52.9 | 0 | 7 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 116 | 0 | 7 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.189× (z -12.3) |
| [[A498 (line)]] | wt | 122 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -10.9) |
| [[BT-474 (line)]] | alt | 65.8 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -10.5) |
| [[LoVo (line)]] | wt | 107 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.209× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 95.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.344× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 79.3 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.300× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[C-33 A (line)]] | alt | 104 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.189× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 56.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.341× (z -8.7) |
| [[COLO 205 (line)]] | alt | 143 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0622× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.185× (z -11.3) |
| [[HOP62 (line)]] | alt | 40.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 34.5 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 46.9 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -9.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 60.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +15.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 91.6 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.266× (z -10.8) |
| [[SW480 (line)]] | alt | 34.8 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.330× (z -11.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-427 (line)]] | wt | 27.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HCT15 (line)]] | alt | 53.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0850× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HT-29 (line)]] | alt | 36.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.311× (z -9.3) |
| [[KATO III (line)]] | alt | 68.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 76.5 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.298× (z -9.1) |
| [[PANC-1 (line)]] | alt | 34.6 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.355× (z -11.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SHP-77 (line)]] | alt | 46.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 63.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 40.4 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0799× (z -9.0) |
| [[H4 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 69.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0681× (z -17.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 64.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[LS 180 (line)]] | wt | 44.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 62.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0573× (z -11.8) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 34.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.102× (z -10.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AN3 CA (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMPK2]] | +0.85 | +0.78 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[USP18]] | +0.84 | +0.81 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 435 |
| [[MX1]] | +0.83 | +0.76 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 432 |
| [[RSAD2]] | +0.83 | +0.76 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 485 |
| [[PARP9]] | +0.83 | +0.74 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 510 |
| [[OAS1]] | +0.83 | +0.75 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 502 |
| [[OAS3]] | +0.82 | +0.74 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 475 |
| [[RIGI]] | +0.82 | +0.74 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 615 |
| [[STAT1]] | +0.82 | +0.71 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[OAS2]] | +0.82 | +0.72 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 433 |
| [[IFIT1]] | +0.81 | +0.75 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 488 |
| [[IFI44]] | +0.80 | +0.74 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 430 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*64 arrows, 64 of them with an alert ⚠; grade A 0, B 36, C 28. Shown: the 12 strongest; 52 more arrows (52 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises TDRD7's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.81× lower at baseline in the lines without OAS2 | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[RSAD2]] | B | RSAD2 activity raises TDRD7's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.77× lower at baseline in the lines without RSAD2 | 0.004 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[NRIR]] | B | NRIR activity raises TDRD7's level | lines that do not express NRIR (14) vs lines expressing it (36) | 1.72× lower at baseline in the lines without NRIR | 0.006 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[DDX60L]] | B | DDX60L activity raises TDRD7's level | lines that do not express DDX60L (7) vs lines expressing it (43) | 1.81× lower at baseline in the lines without DDX60L | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000287188, ENSG00000291144; maybe low, not absent |
| [[GBP4]] | B | GBP4 activity raises TDRD7's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.47× lower at baseline in the lines without GBP4 | 0.010 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[SAMD9]] | B | SAMD9 activity raises TDRD7's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 1.54× lower at baseline in the lines without SAMD9 | 0.013 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[CMPK2]] | B | CMPK2 activity raises TDRD7's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without CMPK2 | 0.016 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[TRIM22]] | B | TRIM22 activity raises TDRD7's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.64× lower at baseline in the lines without TRIM22 | 0.018 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[RASGRP3]] | B | RASGRP3 activity raises TDRD7's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 1.73× lower at baseline in the lines without RASGRP3 | 0.019 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity strengthens TDRD7's drug response | lines that do not express IFI6 (13) vs lines expressing it (36) | the lines without IFI6 respond 0.49× as strongly (z diff +2.36); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.88x vs 0.51x (z diff +3.5) | 0.021 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines |
| [[SAMD9L]] | B | SAMD9L activity raises TDRD7's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.50× lower at baseline in the lines without SAMD9L | 0.024 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[IFI16]] | B | IFI16 activity raises TDRD7's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 1.37× lower at baseline in the lines without IFI16 | 0.024 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARP10]] | C | TDRD7's natural level strengthens PARP10's drug response | TDRD7's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.57; direction not clear | 0.015 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | TDRD7's natural level strengthens USP18's drug response | TDRD7's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.66; direction not clear | 0.017 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PHF11]] | C | TDRD7's natural level strengthens PHF11's drug response | TDRD7's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.63; direction not clear | 0.030 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SAMHD1]] | C | TDRD7's natural level strengthens SAMHD1's drug response | TDRD7's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.61; direction not clear | 0.033 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PSMB9]] | C | TDRD7's natural level strengthens PSMB9's drug response | TDRD7's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.43; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[TRIM14]] | C | TDRD7's natural level strengthens TRIM14's drug response | TDRD7's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.84; direction not clear | 0.044 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PML]] | C | TDRD7's natural level strengthens PML's drug response | TDRD7's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.73; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | TDRD7's natural level strengthens PARP12's drug response | TDRD7's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.64; direction not clear | 0.052 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | TDRD7's natural level strengthens IFIT5's drug response | TDRD7's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.71; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ZC3HAV1]] | C | TDRD7's natural level strengthens ZC3HAV1's drug response | TDRD7's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.04; direction clear | 0.056 | ⚠ tissue can mimic it; precision caveat |
| [[UBE2L6]] | C | TDRD7's natural level strengthens UBE2L6's drug response | TDRD7's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.48; direction not clear | 0.072 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SLC25A28]] | C | TDRD7's natural level strengthens SLC25A28's drug response | TDRD7's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.68; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.5, 54.0); signed map (65.9, 31.8). **Vector** length 119, 42.8% of its response variance represented; |z| ≥ 3 in 1,496 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.78 to 23); *Interferon Signaling* (reactome, mean cos +0.73 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.75 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | -1.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.7 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +4.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | -1.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +1.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.0 | +3.3 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -8.1 | -9.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.2 | -6.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -7.1 | -7.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.1 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -11.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.1 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | tudor domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:97,412,096-97,496,125 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PCTAIRE2BP |
| Gene groups (HGNC) | Tudor domain containing |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHU6](https://www.uniprot.org/uniprotkb/Q8NHU6) (Tudor domain-containing protein 7):

> Component of specific cytoplasmic RNA granules involved in post-transcriptional regulation of specific genes: probably acts by binding to specific mRNAs and regulating their translation. Required for lens transparency during lens development, by regulating translation of genes such as CRYBB3 and HSPB1 in the developing lens. Also required during spermatogenesis.

**Summary**, from NCBI Gene [23424](https://www.ncbi.nlm.nih.gov/gene/23424):

> The protein encoded by this gene belongs to the Tudor family of proteins. This protein contains conserved Tudor domains and LOTUS domains. It is a component of RNA granules, which function in RNA processing. Mutations in this gene have been associated with cataract formation in mouse and human. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2014]

**Accessions** — [HGNC:30831](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30831) · Entrez [23424](https://www.ncbi.nlm.nih.gov/gene/23424) · UniProt [Q8NHU6](https://www.uniprot.org/uniprotkb/Q8NHU6) · Ensembl [ENSG00000196116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196116)

## Data

Gene col 12132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12132); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12132]; `tensor/DDL_lfc|DDL_z.npy` [12132]; `embed/gene_vectors.npy` [12132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12132 or target_col == 12132). Every well: [[TDRD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TDRD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
