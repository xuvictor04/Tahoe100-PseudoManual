---
symbol: "TARS3"
type: "gene"
col: 11674
ensembl_id: "ENSG00000185418"
name: "threonyl-tRNA synthetase 3"
location: "15q26.3"
module: 56
arm: "+"
pooled_cpm: 54.85
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 27
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# TARS3

*threonyl-tRNA synthetase 3* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 1.44× (z +4.1, q 0.024, up in 15 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 3.59×, SW480 1.89×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 1 line (PANC-1 1.93×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (PANC-1 1.91×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.458× (z -16.0, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA2]] (+0.71, fdr 7e-06), [[SLC17A5]] (+0.70, fdr 7e-06), [[RINT1]] (+0.69, fdr 7e-06); moves opposite to [[HNRNPK]] (-0.58, fdr 3e-05), [[PPP2CA]] (-0.55, fdr 2e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11674.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 3.59×, SW480 1.89×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 1 line (PANC-1 1.93×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (PANC-1 1.91×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.024 | 15/49 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trimetrexate (drug)]] 5 µM |  | 1.12× | +3.3 | 0.23 | 3/49 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 1.33× | +3.2 | 0.23 | 15/48 (SHP-77, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.23 | 13/49 (KATO III, LS 180, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.27 | 8/49 (HOP62, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11674.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.458×** | -16.0 | 0e+00 | 39/48 (H4, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.473×** | -16.0 | 0e+00 | 39/48 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.262×** | -15.0 | 0e+00 | 45/49 (NCI-H1792, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.311×** | -13.1 | 8e-37 | 42/48 (RKO, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.555×** | -12.6 | 3e-34 | 35/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.588×** | -11.3 | 1e-27 | 37/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.586×** | -10.5 | 5e-24 | 31/42 (NCI-H460, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.630×** | -9.9 | 5e-21 | 31/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.634×** | -9.7 | 2e-20 | 36/49 (SNU-423, RPMI-7951, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.635×** | -9.3 | 8e-19 | 36/47 (H4, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.649×** | -9.2 | 1e-18 | 34/48 (CFPAC-1, NCI-H1792, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.638×** | -9.2 | 1e-18 | 27/40 (RPMI-7951, HCT15, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.680×** | -8.2 | 1e-14 | 30/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.687×** | -8.0 | 5e-14 | 32/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.712×** | -7.2 | 2e-11 | 31/48 (NCI-H1792, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.721×** | -7.0 | 1e-10 | 28/48 (A549, NCI-H460, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.797×** | -6.5 | 2e-09 | 26/48 (A-172, SNU-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.731×** | -6.2 | 2e-08 | 29/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.750×** | -5.9 | 1e-07 | 26/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.763×** | -5.8 | 2e-07 | 26/48 (A498, HOP62, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.819×** | -4.2 | 5e-04 | 18/48 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.690×** | -4.1 | 8e-04 | 16/48 (PANC-1, SW 1271, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.839× | -3.7 | 0.004 | 17/49 (LS 180, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11674. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 49.6 | 0 | 12 (7 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.260× (z -15.9) |
| [[HOP62 (line)]] | alt | 113 | 0 | 11 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.239× (z -15.0) |
| [[H4 (line)]] | wt | 98.9 | 0 | 10 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0628× (z -20.2) |
| [[RPMI-7951 (line)]] | alt | 88.7 | 0 | 9 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.197× (z -15.0) |
| [[SW480 (line)]] | alt | 46.9 | 1 (1 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | [[TAK-901 (drug)]] 5 µM 0.179× (z -11.5) |
| [[A-172 (line)]] | wt | 50.7 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.160× (z -16.2) |
| [[HS-578T (line)]] | alt | 42.1 | 0 | 8 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -16.8) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.193× (z -14.3) |
| [[A549 (line)]] | wt | 74.4 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.174× (z -18.3) |
| [[PANC-1 (line)]] | alt | 47.7 | 2 (2 ⚠) | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.402× (z -12.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.502× (z -9.7) |
| [[C32 (line)]] | wt | 68.2 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.185× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 52.9 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -13.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.422× (z -8.5) |
| [[SNU-423 (line)]] | alt | 65.0 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.258× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 71.9 | 0 | 5 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.130× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 70.4 | 0 | 5 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -11.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.334× (z -10.5) |
| [[A498 (line)]] | wt | 85.8 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.349× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 31.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.330× (z -8.6) |
| [[LoVo (line)]] | wt | 101 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.422× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 36.4 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.286× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 38.0 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.237× (z -11.7) |
| [[RKO (line)]] | wt | 41.6 | 0 | 3 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0676× (z -11.6) |
| [[SW 900 (line)]] | alt | 66.7 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.313× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 47.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HCT15 (line)]] | alt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[Hs 766T (line)]] | wt | 37.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.139× (z -13.0) |
| [[SNU-1 (line)]] | wt | 65.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.443× (z -8.6) |
| [[A-427 (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | — |
| [[BT-474 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[CHP-212 (line)]] | wt | 49.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.118× (z -12.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[COLO 205 (line)]] | alt | 60.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 48.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HT-29 (line)]] | alt | 52.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.381× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 65.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[KATO III (line)]] | alt | 56.3 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.140× (z -9.2) |
| [[LS 180 (line)]] | wt | 50.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.127× (z -9.2) |
| [[AN3 CA (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11674), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA2]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[SLC17A5]] | +0.70 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[RINT1]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.68 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[COG6]] | +0.67 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[TULP3]] | +0.67 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[NANS]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[EAF2]] | +0.66 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[FAM114A1]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[NPRL2]] | +0.66 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[MINDY2]] | +0.65 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[SEC22A]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK]] | -0.58 | -0.46 / -0.65 | both halves | 3e-05 |  |
| [[PPP2CA]] | -0.55 | -0.46 / -0.57 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.672). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.3, -34.6); signed map (-47.9, 12.3). **Vector** length 111, 32.9% of its response variance represented; |z| ≥ 3 in 1,235 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.50 to 23); *COPI-mediated anterograde transport* (reactome, mean cos +0.52 to 9); *Intra-Golgi and retrograde Golgi-to-ER traffic* (reactome, mean cos +0.51 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.0 | +2.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.9 | +1.8 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.3 | +1.9 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -8.0 | -6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.3 | -16.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.0 | -15.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.4 | -5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -5.4 | -10.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -7.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -13.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.6 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | threonyl-tRNA synthetase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:101,653,596-101,724,473 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25005, ThrRS-L; previously TARSL2 |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Matched by | ensembl_id |

**Function**, from UniProt [A2RTX5](https://www.uniprot.org/uniprotkb/A2RTX5) (Threonine--tRNA ligase 2, cytoplasmic):

> Catalyzes the attachment of threonine to tRNA(Thr) in a two-step reaction: threonine is first activated by ATP to form Thr-AMP and then transferred to the acceptor end of tRNA(Thr). Also edits incorrectly charged tRNA(Thr) via its editing domain, at the post-transfer stage.

**Summary**, from NCBI Gene [123283](https://www.ncbi.nlm.nih.gov/gene/123283):

> Predicted to enable threonine-tRNA ligase activity. Predicted to be involved in threonyl-tRNA aminoacylation. Predicted to be located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24728) · Entrez [123283](https://www.ncbi.nlm.nih.gov/gene/123283) · UniProt [A2RTX5](https://www.uniprot.org/uniprotkb/A2RTX5) · Ensembl [ENSG00000185418](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185418)

## Data

Gene col 11674: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11674); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11674, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11674]; `tensor/DDL_lfc|DDL_z.npy` [11674]; `embed/gene_vectors.npy` [11674]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11674 or target_col == 11674). Every well: [[TARS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TARS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
