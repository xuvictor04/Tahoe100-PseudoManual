---
symbol: "SUGP2"
type: "gene"
col: 751
ensembl_id: "ENSG00000064607"
name: "SURP and G-patch domain containing 2"
location: "19p13"
module: 67
arm: "+"
pooled_cpm: 68.18
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# SUGP2

*SURP and G-patch domain containing 2* — 19p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.64× (z +13.1, q 1e-36, up in 33 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[HI-TOPK-032 (drug)]] 5 µM: 1.31× (z +3.9, q 0.004, up in 12 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.787× (z -9.3, q 6e-18, down in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.561×, LS 180 0.540×, HEC-1-A 0.573×, NCI-H1792 0.552×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (CHP-212 0.219×, SK-MEL-2 0.474×; ⚠ cell-cycle shift, explains ~33% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (SW480 0.558×, HCT15 0.389×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPHOSPH9]] (+0.72, fdr 7e-06), [[ARHGAP11B]] (+0.71, fdr 7e-06), [[NSD2]] (+0.70, fdr 7e-06); moves opposite to [[SNRPB2]] (-0.61, fdr 1e-05), [[SAP18]] (-0.59, fdr 1e-05), [[RPF1]] (-0.56, fdr 1e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PBK]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 751.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.64×** | +13.1 | 1e-36 | 33/43 (LS 180, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.38×** | +8.8 | 3e-16 | 30/49 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +7.7 | 3e-12 | 39/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.28×** | +6.8 | 1e-09 | 26/47 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.27×** | +6.7 | 3e-09 | 27/48 (HT-29, KATO III, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.26×** | +6.3 | 3e-08 | 28/48 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.25×** | +6.1 | 8e-08 | 24/48 (KATO III, SW1417, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.25×** | +6.1 | 9e-08 | 26/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.22×** | +5.5 | 2e-06 | 23/48 (A-427, KATO III, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.21×** | +5.0 | 4e-05 | 23/49 (A-172, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.19× | +4.7 | 1e-04 | 20/48 (COLO 205, Panc 03.27, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | 1.19× | +4.4 | 5e-04 | 19/45 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.004 | 12/48 (A549, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.004 | 14/48 (PANC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.16× | +3.9 | 0.004 | 15/48 (RKO, RPMI-7951, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.011 | 12/48 (RPMI-7951, RKO, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.017 | 15/48 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.023 | 6/48 (NCI-H1792, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.025 | 8/48 (NCI-H661, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.025 | 13/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.037 | 7/49 (RPMI-7951, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.042 | 13/48 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.051 | 4/48 (PANC-1, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 751.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.561×, LS 180 0.540×, HEC-1-A 0.573×, NCI-H1792 0.552×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (CHP-212 0.219×, SK-MEL-2 0.474×; ⚠ cell-cycle shift, explains ~33% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (SW480 0.558×, HCT15 0.389×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.787×** | -9.3 | 6e-18 | 30/48 (CHP-212, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -6.3 | 1e-07 | 0/49 | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.820×** | -5.5 | 7e-06 | 21/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.821×** | -5.5 | 7e-06 | 22/48 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.840× | -4.6 | 4e-04 | 18/48 (A498, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.850× | -4.5 | 6e-04 | 17/48 (PANC-1, SW 1271, …) | all doses, flat | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.892× | -4.5 | 6e-04 | 7/48 (A-427, C-33 A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.892× | -4.5 | 6e-04 | 21/48 (MIA PaCa-2, LS 180, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.872× | -3.8 | 0.009 | 18/48 (C-33 A, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.887× | -3.1 | 0.096 | 14/48 (LoVo, H4, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.856× | -3.1 | 0.11 | 13/48 (Hs 766T, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.897× | -3.0 | 0.13 | 9/48 (NCI-H460, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 751. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 70.2 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.29× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 89.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[CFPAC-1 (line)]] | alt | 33.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[KATO III (line)]] | alt | 31.8 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.74× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A549 (line)]] | wt | 52.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.440× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[C32 (line)]] | wt | 59.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[CHP-212 (line)]] | wt | 81.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.219× (z -12.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 105 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.389× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 63.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 75.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.97× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 28.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H1792 (line)]] | alt | 46.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 70.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 73.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.590× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 85.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.82× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 63.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.474× (z -10.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 99.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.558× (z -9.9) |
| [[A-427 (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 80.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 126 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 99.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 89.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 81.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 751), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH9]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[ARHGAP11B]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[NSD2]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[CENPI]] | +0.68 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[BUB1B]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[TDP1]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[TACC3]] | +0.67 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[CIT]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[DTYMK]] | +0.66 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[KIF18B]] | +0.66 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[CDCA3]] | +0.65 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[WDR62]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB2]] | -0.61 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[SAP18]] | -0.59 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[RPF1]] | -0.56 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[BCAS2]] | -0.56 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PBK]] | C | PBK activity raises SUGP2's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without PBK | 0.017 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises SUGP2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.80× lower at baseline in the lines without AURKB | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MELK]] | C | MELK activity raises SUGP2's level | lines that do not express MELK (3) vs lines expressing it (47) | 1.93× lower at baseline in the lines without MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.8, -52.1); signed map (-44.7, -42.3). **Vector** length 107, 25.1% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.58 to 12); *G2/M checkpoint* (hallmark, mean cos +0.58 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.57 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.1 | +5.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.0 | +6.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +7.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.0 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +3.7 | +13.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.4 | +3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +3.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -8.0 | -9.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -5.6 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | SURP and G-patch domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13 — chr19:18,990,888-19,034,023 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0365; previously SFRS14 |
| Gene groups (HGNC) | G-patch domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IX01](https://www.uniprot.org/uniprotkb/Q8IX01) (SURP and G-patch domain-containing protein 2):

> May play a role in mRNA splicing.

**Summary**, from NCBI Gene [10147](https://www.ncbi.nlm.nih.gov/gene/10147):

> This gene encodes a member of the arginine/serine-rich family of splicing factors. The encoded protein functions in mRNA processing. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:18641](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18641) · Entrez [10147](https://www.ncbi.nlm.nih.gov/gene/10147) · UniProt [Q8IX01](https://www.uniprot.org/uniprotkb/Q8IX01) · Ensembl [ENSG00000064607](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064607)

## Data

Gene col 751: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 751); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 751, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 751]; `tensor/DDL_lfc|DDL_z.npy` [751]; `embed/gene_vectors.npy` [751]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 751 or target_col == 751). Every well: [[SUGP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUGP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
