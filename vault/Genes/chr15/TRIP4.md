---
symbol: "TRIP4"
type: "gene"
col: 2391
ensembl_id: "ENSG00000103671"
name: "thyroid hormone receptor interactor 4"
location: "15q22.31"
module: 12
arm: "+"
pooled_cpm: 43.34
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# TRIP4

*thyroid hormone receptor interactor 4* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.21× (z +5.0, q 2e-04, up in 25 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.30× (z +4.8, q 2e-04, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.449× (z -20.8, q 0e+00, down in 44 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (MIA PaCa-2 0.130×, A498 0.327×, NCI-H460 0.335×, A-172 0.299×, …); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (Panc 03.27 0.0630×, HEC-1-A 0.211×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.249×, AsPC-1 0.294×; ⚠ cell-cycle shift, explains ~59% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C19orf12]] (+0.66, fdr 7e-06), [[KCTD21]] (+0.65, fdr 7e-06), [[PSMF1]] (+0.64, fdr 7e-06); moves opposite to [[PTBP1]] (-0.59, fdr 1e-05), [[FOSB]] (-0.57, fdr 1e-05), [[MBNL3]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2391.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.21×** | +5.0 | 2e-04 | 25/48 (RKO, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +4.9 | 2e-04 | 28/47 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.30×** | +4.8 | 2e-04 | 26/48 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.30×** | +4.8 | 2e-04 | 25/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 0.002 | 20/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.026 | 9/49 (A498, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.0 | 0.17 | 10/48 (HOP62, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2391.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (MIA PaCa-2 0.130×, A498 0.327×, NCI-H460 0.335×, A-172 0.299×, …); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (Panc 03.27 0.0630×, HEC-1-A 0.211×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.249×, AsPC-1 0.294×; ⚠ cell-cycle shift, explains ~59% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.449×** | -20.8 | 0e+00 | 44/48 (MIA PaCa-2, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.624×** | -12.2 | 7e-32 | 35/47 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.554×** | -10.8 | 5e-25 | 38/48 (NCI-H23, C-33 A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.583×** | -9.2 | 8e-18 | 31/42 (Panc 03.27, HEC-1-A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.627×** | -8.2 | 2e-14 | 29/40 (SHP-77, LoVo, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.665×** | -7.5 | 7e-12 | 34/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.726×** | -5.6 | 1e-06 | 27/48 (A-172, SNU-423, …) | rises with dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **0.741×** | -5.3 | 9e-06 | 24/47 (SNU-423, H4, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.744×** | -5.2 | 1e-05 | 28/49 (H4, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.755×** | -5.2 | 1e-05 | 26/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.768×** | -4.8 | 7e-05 | 24/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.764×** | -4.8 | 1e-04 | 25/47 (A-172, RKO, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.785×** | -4.0 | 0.003 | 24/48 (NCI-H460, H4, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.817×** | -3.7 | 0.009 | 21/47 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Gefitinib (drug)]] 5 µM |  | **0.822×** | -3.6 | 0.013 | 14/48 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.842× | -3.0 | 0.081 | 16/47 (BT-474, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2391. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 49.7 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 38.0 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -16.1) |
| [[SNU-423 (line)]] | alt | 53.8 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -15.7) |
| [[LoVo (line)]] | wt | 56.0 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 34.2 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -22.8) |
| [[HEC-1-A (line)]] | alt | 48.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 42.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -15.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 39.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.6) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 57.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 49.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -16.8) |
| [[A549 (line)]] | wt | 67.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 40.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -15.0) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -10.2) |
| [[C32 (line)]] | wt | 33.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -15.0) |
| [[CFPAC-1 (line)]] | alt | 52.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -13.2) ⚠ cell-cycle shift, explains ~59% of this change |
| [[hTERT-HPNE (line)]] | wt | 40.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -12.7) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 43.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 28.4 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.240× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 57.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0630× (z -25.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -15.1) |
| [[PANC-1 (line)]] | alt | 51.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -10.8) |
| [[RKO (line)]] | wt | 34.0 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -9.7) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -8.8) |
| [[SW480 (line)]] | alt | 42.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -9.3) |
| [[BT-474 (line)]] | alt | 39.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -9.5) |
| [[C-33 A (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[HCT15 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[HepG2_C3A (line)]] | wt | 42.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -14.7) |
| [[HOP62 (line)]] | alt | 28.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -12.3) |
| [[Hs 766T (line)]] | wt | 35.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -8.9) |
| [[HS-578T (line)]] | alt | 24.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -13.9) |
| [[J82 (line)]] | alt | 44.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -9.2) |
| [[KATO III (line)]] | alt | 51.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 33.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.0) |
| [[LS 180 (line)]] | wt | 48.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.381× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SHP-77 (line)]] | alt | 62.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SW 900 (line)]] | alt | 28.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -12.6) |
| [[SW1417 (line)]] | alt | 39.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -10.2) |
| [[SW48 (line)]] | wt | 32.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -9.3) |
| [[A-427 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2391), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf12]] | +0.66 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[KCTD21]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PSMF1]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[EYA3]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[NOL7]] ⚠ | +0.62 | +0.52 / +0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SHARPIN]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[COMMD2]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ARPC1A]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[LSP1P4]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ZNF611]] | +0.60 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[EXO5-DT]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CINP]] | +0.59 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[FAM241B]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTBP1]] | -0.59 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[FOSB]] | -0.57 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[MBNL3]] | -0.55 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[RFX3]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[BAHCC1]] | -0.54 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[LINC01135]] | -0.54 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[PRKCG]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[CLOCK]] | -0.53 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[IVNS1ABP]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[GSE1]] | -0.53 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[TFRC]] | -0.52 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[UBR5]] | -0.52 | -0.32 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TRIP4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.362). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-30.1, -5.5); signed map (-17.9, -19.5). **Vector** length 95.4, 23.5% of its response variance represented; |z| ≥ 3 in 893 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.7 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.1 | +2.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +4.5 | +4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.8 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | -0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -20.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.3 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.1 | -12.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.8 | -4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -2.8 | -9.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.3 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | thyroid hormone receptor interactor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:64,387,748-64,455,303 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HsT17391, ZC2HC5, ASC-1 |
| Gene groups (HGNC) | Zinc fingers; Activating signal cointegrator 1 complex |
| Reactome | 3 pathways, smallest: ZNF598 and the Ribosome-associated Quality Trigger (RQT) complex dissociate a ribosome stalled on a no-go mRNA; Ribosome-associated quality control; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15650](https://www.uniprot.org/uniprotkb/Q15650) (Activating signal cointegrator 1):

> Transcription coactivator which associates with nuclear receptors, transcriptional coactivators including EP300, CREBBP and NCOA1, and basal transcription factors like TBP and TFIIA to facilitate nuclear receptors-mediated transcription. May thereby play an important role in establishing distinct coactivator complexes under different cellular conditions. Plays a role in thyroid hormone receptor and estrogen receptor transactivation. Also involved in androgen receptor transactivation (By …

**Summary**, from NCBI Gene [9325](https://www.ncbi.nlm.nih.gov/gene/9325):

> This gene encodes a subunit of the tetrameric nuclear activating signal cointegrator 1 (ASC-1) complex, which associates with transcriptional coactivators, nuclear receptors and basal transcription factors to facilitate nuclear receptors-mediated transcription. This protein is localized in the nucleus and contains an E1A-type zinc finger domain, which mediates interaction with transcriptional coactivators and ligand-bound nuclear receptors, such as thyroid hormone receptor and retinoid X …

**Accessions** — [HGNC:12310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12310) · Entrez [9325](https://www.ncbi.nlm.nih.gov/gene/9325) · UniProt [Q15650](https://www.uniprot.org/uniprotkb/Q15650) · Ensembl [ENSG00000103671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103671)

## Data

Gene col 2391: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2391); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2391, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2391]; `tensor/DDL_lfc|DDL_z.npy` [2391]; `embed/gene_vectors.npy` [2391]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2391 or target_col == 2391). Every well: [[TRIP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
