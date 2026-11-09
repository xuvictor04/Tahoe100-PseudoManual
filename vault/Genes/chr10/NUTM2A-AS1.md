---
symbol: "NUTM2A-AS1"
type: "gene"
col: 13340
ensembl_id: "ENSG00000223482"
name: "NUTM2A antisense RNA 1"
location: "10q23.2"
module: 5
arm: "+"
pooled_cpm: 64.25
n_lines_expressing: 46
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NUTM2A-AS1

*NUTM2A antisense RNA 1* — 10q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.46× (z +8.5, q 2e-14, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.619× (z -10.7, q 4e-24, down in 38 of 44 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (KATO III 0.0803×, A-172 0.220×, A-427 0.307×, A549 0.331×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 0.362×, A498 0.459×, NCI-H1573 0.551×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.316×, A-427 0.365×, HEC-1-A 0.421×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUTM2B-AS1]] (+0.84, fdr 7e-06), [[MFSD14CP-1]] (+0.74, fdr 7e-06), [[RUFY3]] (+0.63, fdr 1e-05); moves opposite to [[DBP]] (-0.58, fdr 1e-05), [[RAB3A]] (-0.58, fdr 1e-05), [[SMAP2]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[ETV1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13340.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +8.5 | 2e-14 | 39/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +7.9 | 6e-13 | 36/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +7.6 | 5e-12 | 38/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +7.2 | 7e-11 | 30/44 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.34×** | +6.3 | 4e-08 | 31/43 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +6.0 | 1e-07 | 27/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.30×** | +5.8 | 4e-07 | 27/44 (CFPAC-1, A498, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +5.1 | 2e-05 | 21/44 (HOP62, SNU-423, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +5.0 | 3e-05 | 22/43 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +5.0 | 4e-05 | 23/44 (HT-29, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.34×** | +4.9 | 6e-05 | 24/44 (HT-29, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +4.6 | 2e-04 | 22/43 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +4.6 | 2e-04 | 23/44 (COLO 205, SNU-423, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.5 | 3e-04 | 13/45 (NCI-H1573, SNU-423, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.22×** | +4.3 | 7e-04 | 18/43 (COLO 205, HT-29, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 7e-04 | 19/43 (A-172, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +4.0 | 0.002 | 20/44 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.5 | 0.011 | 7/44 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.058 | 11/45 (J82, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 13 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13340.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (KATO III 0.0803×, A-172 0.220×, A-427 0.307×, A549 0.331×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 0.362×, A498 0.459×, NCI-H1573 0.551×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.316×, A-427 0.365×, HEC-1-A 0.421×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.619×** | -10.7 | 4e-24 | 38/44 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.640×** | -10.0 | 5e-21 | 38/44 (RKO, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.651×** | -9.2 | 5e-18 | 27/37 (KATO III, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.670×** | -9.0 | 5e-17 | 34/45 (NCI-H1573, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.674×** | -8.8 | 1e-16 | 34/44 (HepG2/C3A, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.780×** | -7.9 | 4e-13 | 27/45 (HEC-1-A, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.749×** | -6.2 | 4e-08 | 25/46 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.870× | -4.4 | 7e-04 | 21/44 (A-172, A498, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **0.826×** | -4.3 | 0.001 | 21/43 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.706×** | -4.1 | 0.003 | 21/43 (C-33 A, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **0.823×** | -4.0 | 0.003 | 21/41 (SW48, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.848× | -3.7 | 0.011 | 19/44 (BT-474, RKO, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.754×** | -3.3 | 0.043 | 18/45 (NCI-H1573, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 75.6 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[A549 (line)]] | wt | 91.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H460 (line)]] | wt | 97.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.27× (z +11.6) | — |
| [[A498 (line)]] | wt | 71.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -15.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 48.5 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -11.6) ⚠ cell-cycle shift, explains ~19% of this change |
| [[HepG2_C3A (line)]] | wt | 100 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.330× (z -10.1) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 89.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[A-427 (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[BT-474 (line)]] | alt | 71.4 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 57.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.8) ⚠ cell-cycle shift, explains ~19% of this change |
| [[MIA PaCa-2 (line)]] | alt | 61.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[NCI-H1573 (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[NCI-H2030 (line)]] | alt | 65.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[RKO (line)]] | wt | 103 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.429× (z -9.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[C-33 A (line)]] | alt | 96.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[HOP62 (line)]] | alt | 66.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.15× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 74.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[HT-29 (line)]] | alt | 70.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.27× (z +8.6) | — |
| [[KATO III (line)]] | alt | 49.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0803× (z -25.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[LoVo (line)]] | wt | 80.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.527× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[LOX-IMVI (line)]] | wt | 89.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.467× (z -9.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H23 (line)]] | alt | 70.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[PANC-1 (line)]] | alt | 79.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +11.0) | — |
| [[SW1417 (line)]] | alt | 86.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.461× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[AN3 CA (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.15 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.25 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUTM2B-AS1]] | +0.84 | +0.73 / +0.85 | both halves | 7e-06 | same gene group |
| [[MFSD14CP-1]] | +0.74 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[RUFY3]] | +0.63 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[LRRC69]] | +0.62 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[KIAA0232]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[ACYP2]] | +0.59 | +0.34 / +0.65 | both halves | 1e-04 |  |
| [[POU6F1]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CDC42BPA]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[CUEDC1]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[C1orf159]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | +0.57 | +0.42 / +0.54 | both halves | 4e-05 | same gene group |
| [[PHYKPL]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBP]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[RAB3A]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[SMAP2]] | -0.58 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[MDH1]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[SPICE1]] | -0.56 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[ZNF395]] | -0.55 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[ACADSB]] | -0.55 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[MIDEAS]] | -0.55 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[ORC4]] | -0.54 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[RARA]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[ELP3]] | -0.53 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[KDM5B]] | -0.53 | -0.61 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETV1]] | C | NUTM2A-AS1 activity lowers ETV1's level | lines that do not express NUTM2A-AS1 (4) vs lines expressing it (46) | 4.50× higher at baseline in the lines without NUTM2A-AS1 | 0.043 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ISG15, ENSG00000285257, BIRC3; maybe low, not absent |
| [[TXNRD1]] | C | NUTM2A-AS1 activity raises TXNRD1's level | lines that do not express NUTM2A-AS1 (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without NUTM2A-AS1 | 0.053 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ISG15, ENSG00000285257, BIRC3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.435). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (7.1, -11.4); signed map (10.0, -6.7). **Vector** length 100, 24.9% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.7 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.8 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.5 | +4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.2 | +5.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.5 | +4.5 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.1 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -0.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -3.4 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.5 | -10.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -2.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | NUTM2A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q23.2 — chr10:87,189,773-87,342,612 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously FAM22A-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:45161](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:45161) · Entrez [728190](https://www.ncbi.nlm.nih.gov/gene/728190) · Ensembl [ENSG00000223482](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223482)

## Data

Gene col 13340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13340); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13340]; `tensor/DDL_lfc|DDL_z.npy` [13340]; `embed/gene_vectors.npy` [13340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13340 or target_col == 13340). Every well: [[NUTM2A-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUTM2A-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
