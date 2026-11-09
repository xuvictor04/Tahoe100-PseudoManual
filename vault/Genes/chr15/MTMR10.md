---
symbol: "MTMR10"
type: "gene"
col: 9386
ensembl_id: "ENSG00000166912"
name: "myotubularin related protein 10"
location: "15q13.3"
module: 17
arm: "+"
pooled_cpm: 40.5
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MTMR10

*myotubularin related protein 10* — 15q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.35× (z +6.9, q 3e-09, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.578× (z -8.9, q 3e-16, down in 31 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.689× (z -6.0, q 3e-07, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1792 0.0513×, A-172 0.293×, HOP62 0.339×, KATO III 0.303×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HEC-1-A 0.251×, A-427 0.212×, NCI-H2030 0.281×, KATO III 0.292×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.233×, AsPC-1 0.424×; ⚠ cell-cycle shift, explains ~21% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (HT-29 0.355×); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.326×); [[OTS514 (drug)]] 5 µM in 1 line (SHP-77 0.103×).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNKSR1]] (+0.56, fdr 2e-05), [[HDAC11]] (+0.52, fdr 3e-05), [[DDX19B]] (+0.52, fdr 3e-05); moves opposite to [[PRDM15]] (-0.50, fdr 3e-04), [[BANP]] (-0.49, fdr 2e-05), [[DEGS1]] (-0.48, fdr 7e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9386.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +6.9 | 3e-09 | 32/48 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.035 | 20/48 (A-172, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.047 | 21/49 (PANC-1, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 1.48× | +3.3 | 0.12 | 16/48 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.22× | +3.1 | 0.21 | 13/47 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.21× | +3.1 | 0.21 | 11/47 (AsPC-1, LoVo, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9386.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1792 0.0513×, A-172 0.293×, HOP62 0.339×, KATO III 0.303×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HEC-1-A 0.251×, A-427 0.212×, NCI-H2030 0.281×, KATO III 0.292×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.233×, AsPC-1 0.424×; ⚠ cell-cycle shift, explains ~21% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (HT-29 0.355×); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.326×); [[OTS514 (drug)]] 5 µM in 1 line (SHP-77 0.103×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.578×** | -8.9 | 3e-16 | 31/44 (HEC-1-A, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.566×** | -8.5 | 4e-15 | 30/42 (CFPAC-1, LS 180, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.689×** | -6.0 | 3e-07 | 27/47 (C32, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.769×** | -6.0 | 3e-07 | 27/48 (HT-29, AsPC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.693×** | -5.7 | 1e-06 | 24/39 (NCI-H1792, A-172, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.790×** | -5.4 | 6e-06 | 27/48 (CFPAC-1, A549, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.764×** | -4.4 | 0.001 | 22/47 (AsPC-1, A549, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.778×** | -3.9 | 0.006 | 21/48 (HT-29, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.779×** | -3.9 | 0.006 | 21/46 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.862× | -3.4 | 0.038 | 18/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.814×** | -3.2 | 0.071 | 17/47 (HS-578T, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 0.828× | -3.1 | 0.11 | 20/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9386. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 28.2 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HT-29 (line)]] | alt | 140 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -13.5) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.355× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 46.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[KATO III (line)]] | alt | 53.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H2030 (line)]] | alt | 42.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A-427 (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[BT-474 (line)]] | alt | 25.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.1) | — |
| [[C32 (line)]] | wt | 48.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.326× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 39.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HOP62 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[MIA PaCa-2 (line)]] | alt | 22.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0513× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[SHP-77 (line)]] | alt | 32.0 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.103× (z -8.7) |
| [[SW480 (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.427× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[A498 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9386), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNKSR1]] | +0.56 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[HDAC11]] | +0.52 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[DDX19B]] | +0.52 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[WDR11]] | +0.51 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[PLCD3]] | +0.51 | +0.46 / +0.37 | both halves | 9e-05 |  |
| [[BBS5]] | +0.51 | +0.55 / +0.28 | both halves | 3e-04 |  |
| [[ABCG1]] | +0.49 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[ZNF205]] | +0.47 | +0.43 / +0.29 | both halves | 3e-04 |  |
| [[FAM221A]] | +0.46 | +0.47 / +0.16 | ⚠ not reproduced | 0.001 |  |
| [[CCNDBP1]] | +0.46 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[GSKIP]] | +0.46 | +0.43 / +0.27 | both halves | 3e-04 |  |
| [[FRG1GP]] | +0.45 | +0.45 / +0.19 | ⚠ not reproduced | 9e-04 |  |
| [[RAB11A]] | +0.45 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[KDM1B]] | +0.45 | +0.49 / +0.29 | both halves | 3e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM15]] | -0.50 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[BANP]] | -0.49 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[DEGS1]] | -0.48 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[ZNF407]] | -0.47 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[PRDM10]] | -0.46 | -0.45 / -0.21 | both halves | 7e-04 |  |
| [[ZNF876P]] | -0.45 | -0.39 / -0.27 | both halves | 3e-04 |  |
| [[DRC1]] | -0.43 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[MZF1]] | -0.43 | -0.43 / -0.22 | both halves | 6e-04 |  |
| [[FBLN7]] | -0.43 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[SLC6A16]] | -0.43 | -0.43 / -0.21 | both halves | 6e-04 |  |
| [[BCO2]] | -0.43 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[CYCS]] | -0.42 | -0.37 / -0.43 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MTMR10's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF876P]] | B | ZNF876P activity lowers MTMR10's level | lines that do not express ZNF876P (17) vs lines expressing it (33) | 1.35× higher at baseline in the lines without ZNF876P | 0.014 | ⚠ within organs, on part of the lines; also absent: ZNF718, PAX8 |
| [[IL2RG]] | B | IL2RG activity raises MTMR10's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.19× lower at baseline in the lines without IL2RG | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[IL2RG]] | B | IL2RG activity strengthens MTMR10's drug response | lines that do not express IL2RG (25) vs lines expressing it (23) | the lines without IL2RG respond 0.77× as strongly (z diff +0.60); strongest at Idarubicin (hydrochloride) 5 µM: 0.87x vs 0.67x (z diff +2.6) | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.399). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-10.4, 28.9); signed map (-22.8, -15.0). **Vector** length 72.6, 13.5% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +6.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.0 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | -0.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.4 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | -0.0 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -3.6 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | myotubularin related protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.3 — chr15:30,938,941-30,991,628 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20313 |
| Gene groups (HGNC) | Myotubularins |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the early endosome membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

UniProt [Q9NXD2](https://www.uniprot.org/uniprotkb/Q9NXD2) carries no function annotation.

**Summary**, from NCBI Gene [54893](https://www.ncbi.nlm.nih.gov/gene/54893):

> Located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25999) · Entrez [54893](https://www.ncbi.nlm.nih.gov/gene/54893) · UniProt [Q9NXD2](https://www.uniprot.org/uniprotkb/Q9NXD2) · Ensembl [ENSG00000166912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166912)

## Data

Gene col 9386: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9386); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9386, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9386]; `tensor/DDL_lfc|DDL_z.npy` [9386]; `embed/gene_vectors.npy` [9386]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9386 or target_col == 9386). Every well: [[MTMR10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTMR10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
