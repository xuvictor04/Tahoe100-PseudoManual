---
symbol: "CRLS1"
type: "gene"
col: 1542
ensembl_id: "ENSG00000088766"
name: "cardiolipin synthase 1"
location: "20p12.3"
module: 40
arm: "+"
pooled_cpm: 73.45
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# CRLS1

*cardiolipin synthase 1* — 20p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.28× (z +4.6, q 0.002, up in 27 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.34×).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.360× (z -13.9, q 6e-41, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.494× (z -9.2, q 6e-18, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM39A]] (+0.74, fdr 7e-06), [[TXNDC11]] (+0.73, fdr 7e-06), [[DNAJC25]] (+0.72, fdr 7e-06); moves opposite to [[DST]] (-0.61, fdr 7e-06), [[ATF7IP]] (-0.59, fdr 1e-05), [[ANKLE2]] (-0.59, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1542.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.34×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.6 | 0.002 | 27/49 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1542.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.360×** | -13.9 | 6e-41 | 47/49 (H4, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.385×** | -12.5 | 3e-33 | 41/43 (SW 900, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.494×** | -9.2 | 6e-18 | 41/48 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.531×** | -8.0 | 2e-13 | 40/45 (SW 900, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.656×** | -7.9 | 2e-13 | 34/48 (HepG2/C3A, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.610×** | -6.7 | 2e-09 | 37/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.642×** | -6.0 | 1e-07 | 35/48 (C32, SW 900, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.664×** | -5.6 | 2e-06 | 36/48 (CFPAC-1, NCI-H2347, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.665×** | -5.5 | 2e-06 | 39/48 (HS-578T, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.684×** | -5.2 | 1e-05 | 31/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -5.1 | 2e-05 | 34/47 (SHP-77, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.703×** | -4.8 | 8e-05 | 33/48 (SW 1088, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **0.715×** | -4.6 | 2e-04 | 34/48 (HepG2/C3A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.722×** | -4.3 | 8e-04 | 30/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.738×** | -4.1 | 0.001 | 33/48 (MIA PaCa-2, COLO 205, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.763×** | -3.7 | 0.008 | 29/48 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.766×** | -3.6 | 0.009 | 25/48 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.774×** | -3.5 | 0.015 | 28/48 (H4, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.778×** | -3.4 | 0.017 | 26/49 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.786×** | -3.3 | 0.026 | 23/48 (HepG2/C3A, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.787×** | -3.3 | 0.027 | 27/49 (LOX-IMVI, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1542. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 191 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.271× (z -10.7) |
| [[A549 (line)]] | wt | 119 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -14.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.289× (z -11.3) |
| [[HS-578T (line)]] | alt | 102 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -11.4) |
| [[A-172 (line)]] | wt | 59.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -14.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.228× (z -13.8) |
| [[RPMI-7951 (line)]] | alt | 119 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.289× (z -10.5) |
| [[SW 900 (line)]] | alt | 128 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0673× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.300× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 95.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.388× (z -8.5) |
| [[HOP62 (line)]] | alt | 112 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.319× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 87.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -9.3) |
| [[H4 (line)]] | wt | 104 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0318× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.185× (z -11.2) |
| [[A498 (line)]] | wt | 60.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.355× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 86.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -13.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 54.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -16.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 74.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 50.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -16.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 62.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.383× (z -9.1) |
| [[SHP-77 (line)]] | alt | 79.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.317× (z -10.8) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 61.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -8.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 70.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -11.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 37.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -12.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 58.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -11.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 57.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -12.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 72.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -13.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 88.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 76.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -8.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 50.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -10.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 91.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -8.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 73.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 60.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.346× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 59.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -9.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 49.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -10.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -12.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -14.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0942× (z -10.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -9.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 66.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 82.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -12.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 88.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1542), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM39A]] | +0.74 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.73 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[RINT1]] | +0.71 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[RARS2]] | +0.70 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[EEF1AKMT4]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[MED26]] | +0.70 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[PDIA5]] | +0.68 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[OXNAD1]] | +0.68 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.68 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[THOC3]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DST]] | -0.61 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[ATF7IP]] | -0.59 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[ANKLE2]] | -0.59 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[MPDZ]] | -0.58 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[ZNF518B]] | -0.58 | -0.55 / -0.67 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.754). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (7.7, -31.8); signed map (-47.4, 7.7). **Vector** length 125, 41.4% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.4 | -2.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.4 | +2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.3 | +2.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.1 | +0.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.7 | +0.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.7 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.8 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -5.2 | -7.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.5 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -3.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | cardiolipin synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.3 — chr20:6,006,093-6,040,053 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ967N21.6, CLS1, GCD10; previously C20orf155 |
| Reactome | 4 pathways, smallest: Acyl chain remodelling of PG; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJA2](https://www.uniprot.org/uniprotkb/Q9UJA2) (Cardiolipin synthase):

> Catalyzes the synthesis of cardiolipin (CL) (diphosphatidylglycerol) by specifically transferring a phosphatidyl group from CDP-diacylglycerol to phosphatidylglycerol (PG). CL is a key phospholipid in mitochondrial membranes and plays important roles in maintaining the functional integrity and dynamics of mitochondria under both optimal and stress conditions.

**Summary**, from NCBI Gene [54675](https://www.ncbi.nlm.nih.gov/gene/54675):

> This gene encodes a member of the CDP-alcohol phosphatidyltransferase class-I family of proteins. The encoded enzyme catalyzes the synthesis of cardiolipin, a phospholipid component of mitochondrial membranes that is critical for mitochondrial function. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:16148](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16148) · Entrez [54675](https://www.ncbi.nlm.nih.gov/gene/54675) · UniProt [Q9UJA2](https://www.uniprot.org/uniprotkb/Q9UJA2) · Ensembl [ENSG00000088766](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088766)

## Data

Gene col 1542: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1542); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1542, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1542]; `tensor/DDL_lfc|DDL_z.npy` [1542]; `embed/gene_vectors.npy` [1542]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1542 or target_col == 1542). Every well: [[CRLS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRLS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
