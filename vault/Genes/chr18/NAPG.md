---
symbol: "NAPG"
type: "gene"
col: 5534
ensembl_id: "ENSG00000134265"
name: "NSF attachment protein gamma"
location: "18p11.22"
module: 199
arm: "+"
pooled_cpm: 85.91
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# NAPG

*NSF attachment protein gamma* — 18p11.22

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 3.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.558× (z -21.9, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCAF13]] (+0.69, fdr 7e-06), [[STRAP]] (+0.66, fdr 1e-05), [[GDAP2]] (+0.63, fdr 1e-05); moves opposite to [[DNAI4]] (-0.70, fdr 3e-05), [[ZC3H6]] (-0.66, fdr 7e-06), [[ZBTB25]] (-0.64, fdr 2e-05).
> It is in [[Module 199]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5534.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 3.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.19× | +4.7 | 0.001 | 19/48 (C32, LS 180, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.097 | 6/48 (SW 900, LOX-IMVI, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.05 µM |  | 1.13× | +3.4 | 0.11 | 6/48 (NCI-H2347, LS 180, …) | all doses, flat | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.13× | +3.4 | 0.11 | 8/48 (NCI-H2030, HOP62, …) | all doses, flat | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.25 | 2/49 (Panc 03.27, SNU-423) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5534.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.558×** | -21.9 | 0e+00 | 43/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.585×** | -20.1 | 0e+00 | 43/49 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.616×** | -12.4 | 8e-33 | 40/48 (NCI-H1792, A498, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.659×** | -11.1 | 3e-26 | 35/48 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.701×** | -9.4 | 4e-19 | 32/48 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.741×** | -7.6 | 2e-12 | 35/48 (A498, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.757×** | -7.4 | 1e-11 | 32/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.764×** | -7.2 | 6e-11 | 27/48 (H4, NCI-H1792, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **0.781×** | -6.6 | 4e-09 | 29/48 (SW 900, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.785×** | -6.4 | 8e-09 | 23/48 (A-172, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.786×** | -6.1 | 4e-08 | 26/50 (AsPC-1, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.819×** | -5.3 | 6e-06 | 21/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | 0.836× | -4.8 | 9e-05 | 24/49 (SHP-77, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | 0.838× | -4.7 | 1e-04 | 22/48 (SW 900, Panc 03.27, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.883× | -4.7 | 1e-04 | 12/48 (NCI-H2347, SNU-1, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.849× | -4.3 | 5e-04 | 17/48 (SW 900, SW48, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.896× | -4.1 | 0.001 | 9/48 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.895× | -3.6 | 0.011 | 10/48 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.884× | -3.3 | 0.029 | 8/47 (NCI-H23, A549, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.901× | -3.2 | 0.032 | 8/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5534. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 80.6 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -18.4) |
| [[AsPC-1 (line)]] | alt | 150 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -30.1) |
| [[HOP62 (line)]] | alt | 106 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.364× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 53.8 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.193× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 49.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -17.3) |
| [[A-172 (line)]] | wt | 66.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -12.3) |
| [[H4 (line)]] | wt | 72.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -12.8) |
| [[SW 900 (line)]] | alt | 115 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -17.2) |
| [[HS-578T (line)]] | alt | 105 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -14.8) |
| [[hTERT-HPNE (line)]] | wt | 69.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -12.6) |
| [[LoVo (line)]] | wt | 88.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 134 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 100 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -9.6) |
| [[RKO (line)]] | wt | 53.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -9.6) |
| [[SW1417 (line)]] | alt | 145 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -13.3) |
| [[A549 (line)]] | wt | 65.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -14.6) |
| [[HepG2_C3A (line)]] | wt | 70.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 80.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -12.0) |
| [[LS 180 (line)]] | wt | 122 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 82.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -11.3) |
| [[PANC-1 (line)]] | alt | 70.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -17.1) |
| [[SW48 (line)]] | wt | 154 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -10.6) |
| [[SW480 (line)]] | alt | 135 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -13.5) |
| [[A-427 (line)]] | wt | 115 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -18.0) |
| [[BT-474 (line)]] | alt | 118 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.8) |
| [[COLO 205 (line)]] | alt | 87.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -12.6) |
| [[Hs 766T (line)]] | wt | 80.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -8.7) |
| [[J82 (line)]] | alt | 65.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -11.4) |
| [[KATO III (line)]] | alt | 67.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 73.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 88.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.610× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -14.7) |
| [[SHP-77 (line)]] | alt | 59.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SNU-423 (line)]] | alt | 41.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -10.9) |
| [[AN3 CA (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 88.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 96.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5534), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF13]] | +0.69 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[STRAP]] | +0.66 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[GDAP2]] | +0.63 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[TAF5L]] | +0.63 | +0.71 / +0.35 | both halves | 1e-04 |  |
| [[GTF2E2]] | +0.62 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[EFCAB14]] | +0.62 | +0.74 / +0.46 | both halves | 2e-05 |  |
| [[RSU1]] | +0.62 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[ATG5]] | +0.61 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[PAFAH1B2]] | +0.61 | +0.69 / +0.34 | both halves | 1e-04 | pathway: Golgi-to-ER retrograde transport |
| [[SMC5]] | +0.61 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[FBXW2]] | +0.61 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[GNAI3]] | +0.61 | +0.69 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAI4]] | -0.70 | -0.72 / -0.45 | both halves | 3e-05 |  |
| [[ZC3H6]] | -0.66 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[ZBTB25]] | -0.64 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[IRF2]] | -0.64 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[GALNT7-DT]] | -0.64 | -0.72 / -0.24 | both halves | 4e-04 |  |
| [[PLS3-AS1]] | -0.62 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[STAP2]] | -0.62 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.61 | -0.65 / -0.32 | both halves | 2e-04 |  |
| [[ENTPD3-AS1]] | -0.61 | -0.62 / -0.29 | both halves | 2e-04 |  |
| [[UNK]] | -0.61 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[SBF2-AS1]] | -0.61 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[TAPBPL]] | -0.60 | -0.66 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NAPG's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF441]] | B | ZNF441 activity raises NAPG's level | lines that do not express ZNF441 (7) vs lines expressing it (43) | 1.31× lower at baseline in the lines without ZNF441 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000286098, ZNF442, ZNF433 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.4, -28.3); signed map (-49.8, -4.0). **Vector** length 99.6, 24.2% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.9 | +4.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.8 | +3.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.7 | +3.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.9 | -21.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -20.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -12.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -7.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.9 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.0 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | NSF attachment protein gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.22 — chr18:10,525,905-10,552,764 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 12 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; COPII-mediated vesicle transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99747](https://www.uniprot.org/uniprotkb/Q99747) (Gamma-soluble NSF attachment protein):

> Required for vesicular transport between the endoplasmic reticulum and the Golgi apparatus.

**Summary**, from NCBI Gene [8774](https://www.ncbi.nlm.nih.gov/gene/8774):

> This gene encodes soluble NSF attachment protein gamma. The soluble NSF attachment proteins (SNAPs) enable N-ethyl-maleimide-sensitive fusion protein (NSF) to bind to target membranes. NSF and SNAPs appear to be general components of the intracellular membrane fusion apparatus, and their action at specific sites of fusion must be controlled by SNAP receptors particular to the membranes being fused. The product of this gene mediates platelet exocytosis and controls the membrane fusion events of …

**Accessions** — [HGNC:7642](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7642) · Entrez [8774](https://www.ncbi.nlm.nih.gov/gene/8774) · UniProt [Q99747](https://www.uniprot.org/uniprotkb/Q99747) · Ensembl [ENSG00000134265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134265)

## Data

Gene col 5534: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5534); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5534, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5534]; `tensor/DDL_lfc|DDL_z.npy` [5534]; `embed/gene_vectors.npy` [5534]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5534 or target_col == 5534). Every well: [[NAPG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAPG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
