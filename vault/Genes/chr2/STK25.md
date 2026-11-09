---
symbol: "STK25"
type: "gene"
col: 3712
ensembl_id: "ENSG00000115694"
name: "serine/threonine kinase 25"
location: "2q37.3"
module: 2
arm: "+"
pooled_cpm: 22.02
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# STK25

*serine/threonine kinase 25* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.27× (z +12.8, q 2e-34, up in 27 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.35× (z +4.6, q 6e-04, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1792 4.91×, PANC-1 2.76×, MIA PaCa-2 3.57×, LOX-IMVI 4.22×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (PANC-1 2.59×, A498 2.92×, NCI-H460 2.52×, LS 180 3.52×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.353× (z -23.8, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPKAPK3]] (+0.72, fdr 7e-06), [[INTS11]] (+0.72, fdr 1e-05), [[SH3GLB2]] (+0.70, fdr 1e-05); moves opposite to [[NDUFC1]] (-0.63, fdr 2e-05), [[PNISR]] (-0.61, fdr 3e-05), [[SCAF11]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3712.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H1792 4.91×, PANC-1 2.76×, MIA PaCa-2 3.57×, LOX-IMVI 4.22×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (PANC-1 2.59×, A498 2.92×, NCI-H460 2.52×, LS 180 3.52×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +12.8 | 2e-34 | 27/32 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +11.5 | 4e-28 | 35/42 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +6.7 | 4e-09 | 24/36 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +4.6 | 6e-04 | 24/48 (PANC-1, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +4.0 | 0.007 | 17/44 (RPMI-7951, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +3.3 | 0.079 | 14/43 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3712.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.353×** | -23.8 | 0e+00 | 47/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.465×** | -12.4 | 7e-33 | 43/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.475×** | -12.1 | 4e-31 | 38/47 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.522×** | -10.5 | 9e-24 | 38/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.586×** | -8.7 | 5e-16 | 39/48 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.611×** | -8.0 | 1e-13 | 36/47 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -7.9 | 3e-13 | 30/47 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.635×** | -7.1 | 9e-11 | 33/48 (J82, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.448×** | -6.8 | 7e-10 | 36/48 (NCI-H23, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.740×** | -4.9 | 6e-05 | 22/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.757×** | -4.5 | 3e-04 | 20/47 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.637×** | -3.8 | 0.006 | 23/45 (Panc 03.27, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.813×** | -3.4 | 0.034 | 18/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.034 | 16/47 (J82, AN3 CA, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.870× | -3.2 | 0.052 | 16/48 (MIA PaCa-2, PANC-1, …) | top dose only | low cells (technical?) |
| [[Tadalafil (drug)]] 5 µM |  | **0.823×** | -3.1 | 0.080 | 13/47 (COLO 205, NCI-H2030, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 26.0 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 22.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -21.9) |
| [[HEC-1-A (line)]] | alt | 33.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -12.0) |
| [[HT-29 (line)]] | alt | 21.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 18.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -17.0) |
| [[MIA PaCa-2 (line)]] | alt | 28.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +9.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -11.9) |
| [[PANC-1 (line)]] | alt | 26.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -15.9) |
| [[A-427 (line)]] | wt | 26.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.451× (z -8.7) |
| [[A498 (line)]] | wt | 16.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -11.0) |
| [[HOP62 (line)]] | alt | 25.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.7) |
| [[LS 180 (line)]] | wt | 23.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 24.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.91× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 21.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -14.2) |
| [[SW48 (line)]] | wt | 21.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -10.6) |
| [[SW480 (line)]] | alt | 18.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.0) |
| [[A-172 (line)]] | wt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -8.8) |
| [[A549 (line)]] | wt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.8) |
| [[AN3 CA (line)]] | alt | 26.7 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.05 µM 0.0622× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.6) |
| [[BT-474 (line)]] | alt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.0) |
| [[C-33 A (line)]] | alt | 33.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.0) |
| [[C32 (line)]] | wt | 9.06 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.120× (z -9.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -14.2) |
| [[H4 (line)]] | wt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -15.1) |
| [[HCT15 (line)]] | alt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.5) |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -9.7) |
| [[HS-578T (line)]] | alt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.1) |
| [[J82 (line)]] | alt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -12.9) |
| [[KATO III (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -14.3) |
| [[NCI-H2347 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -13.5) |
| [[RKO (line)]] | wt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.9) |
| [[SNU-1 (line)]] | wt | 29.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.186× (z -8.9) |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -8.5) |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -8.8) |
| [[SW1417 (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -9.2) |
| [[CHP-212 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK3]] | +0.72 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[INTS11]] | +0.72 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[SH3GLB2]] | +0.70 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[ZDHHC8]] | +0.68 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[HSF1]] | +0.67 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[E2F4]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PCNX3]] | +0.66 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[TCF3]] | +0.66 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[CSK]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[BLTP2]] | +0.64 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[CPSF1]] | +0.64 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ADAMTSL5]] | +0.64 | +0.62 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFC1]] | -0.63 | -0.65 / -0.46 | both halves | 2e-05 |  |
| [[PNISR]] | -0.61 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[SCAF11]] | -0.60 | -0.66 / -0.36 | both halves | 1e-04 |  |
| [[STAP2]] | -0.60 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[ATP23]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[FMC1]] | -0.59 | -0.61 / -0.39 | both halves | 6e-05 |  |
| [[TERF2IP]] | -0.59 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[DICER1-AS1]] | -0.58 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[MITD1]] | -0.58 | -0.71 / -0.39 | both halves | 5e-05 |  |
| [[ZC3H6]] | -0.58 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[CCDC170]] | -0.58 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ARID4B]] | -0.57 | -0.55 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.4, -23.5); signed map (-45.3, -10.2). **Vector** length 67.7, 12.3% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | -1.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.0 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | -1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.2 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -23.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -12.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | -10.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,492,670-241,509,730 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SOK1, YSK1 |
| Gene groups (HGNC) | STRIPAK complex; STK24/STK25/ST26 kinase family |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, UV_RESPONSE_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [O00506](https://www.uniprot.org/uniprotkb/O00506) (Serine/threonine-protein kinase 25):

> Oxidant stress-activated serine/threonine kinase that plays a role in metabolic homeostasis, neuronal polarization, cell migration, Golgi organization, apoptosis or innate immunity. Targets to the Golgi apparatus where it appears to regulate protein transport events, cell adhesion, and polarity complexes important for cell migration. Part of the striatin-interacting phosphatase and kinase (STRIPAK) complexes. STRIPAK complexes have critical roles in protein (de)phosphorylation and are …

**Summary**, from NCBI Gene [10494](https://www.ncbi.nlm.nih.gov/gene/10494):

> This gene encodes a member of the germinal centre kinase III (GCK III) subfamily of the sterile 20 superfamily of kinases. The encoded enzyme plays a role in serine-threonine liver kinase B1 (LKB1) signaling pathway to regulate neuronal polarization and morphology of the Golgi apparatus. The protein is translocated from the Golgi apparatus to the nucleus in response to chemical anoxia and plays a role in regulation of cell death. A pseudogene associated with this gene is located on chromosome …

**Accessions** — [HGNC:11404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11404) · Entrez [10494](https://www.ncbi.nlm.nih.gov/gene/10494) · UniProt [O00506](https://www.uniprot.org/uniprotkb/O00506) · Ensembl [ENSG00000115694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115694)

## Data

Gene col 3712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3712); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3712]; `tensor/DDL_lfc|DDL_z.npy` [3712]; `embed/gene_vectors.npy` [3712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3712 or target_col == 3712). Every well: [[STK25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
