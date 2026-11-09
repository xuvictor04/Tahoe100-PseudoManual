---
symbol: "ESCO1"
type: "gene"
col: 6520
ensembl_id: "ENSG00000141446"
name: "establishment of sister chromatid cohesion N-acetyltransferase 1"
location: "18q11.2"
module: 41
arm: "+"
pooled_cpm: 118.52
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ESCO1

*establishment of sister chromatid cohesion N-acetyltransferase 1* — 18q11.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 2.01×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.397× (z -16.6, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.772× (z -6.6, q 5e-09, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL28]] (+0.70, fdr 7e-06), [[SRP54]] (+0.68, fdr 7e-06), [[MINDY2]] (+0.68, fdr 7e-06); moves opposite to [[LPP]] (-0.59, fdr 1e-05), [[MAPRE1]] (-0.58, fdr 1e-05), [[CDC42BPA]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 2.01×; ⚠ cell-cycle shift, explains ~0% of this change).

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 16 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6520.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.397×** | -16.6 | 0e+00 | 46/49 (AsPC-1, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.368×** | -16.6 | 0e+00 | 41/45 (NCI-H1792, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.404×** | -15.6 | 0e+00 | 44/44 (A-427, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -9.6 | 1e-19 | 41/47 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.673×** | -7.1 | 1e-10 | 36/48 (COLO 205, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.772×** | -6.6 | 5e-09 | 37/48 (A-172, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.699×** | -6.4 | 1e-08 | 34/48 (C32, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.727×** | -5.5 | 3e-06 | 29/48 (A498, NCI-H1792, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.807×** | -5.4 | 4e-06 | 25/49 (A549, SNU-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.739×** | -5.2 | 1e-05 | 30/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.740×** | -5.2 | 1e-05 | 33/48 (LoVo, C32, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.757×** | -5.0 | 3e-05 | 32/48 (C32, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.764×** | -4.8 | 6e-05 | 26/48 (C32, CFPAC-1, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.828×** | -4.8 | 7e-05 | 19/48 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.780×** | -4.5 | 3e-04 | 26/48 (A498, C32, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.841× | -3.1 | 0.052 | 17/48 (LS 180, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 134 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.519× (z -10.9) |
| [[C32 (line)]] | wt | 125 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 120 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 86.2 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -12.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 161 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 224 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 191 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 91.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -12.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 90.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 127 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0670× (z -34.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -14.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 117 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -12.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 186 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -15.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 116 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 133 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -19.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 98.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -11.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 145 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -16.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 108 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.433× (z -9.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 124 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -14.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 103 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -11.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 192 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 106 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 92.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -14.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 82.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -12.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 98.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -12.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 103 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 179 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -10.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 160 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -15.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 101 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -11.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[CHP-212 (line)]] | wt | 87.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -12.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -10.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.325× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 99.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 97.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -11.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6520), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL28]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SRP54]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[MINDY2]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[RARS1]] | +0.67 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[TGDS]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[NOSIP]] | +0.65 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SEC22A]] | +0.65 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[RINT1]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[ACBD3]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TBC1D20]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[DIS3]] | +0.64 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[DDX50]] | +0.64 | +0.58 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPP]] | -0.59 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.58 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[CDC42BPA]] | -0.55 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ZNF236]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[LINC00342]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (6.8, -33.2); signed map (-46.6, 13.8). **Vector** length 101, 31.1% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Retinoic acid (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.3 | -5.4 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +2.2 | +2.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +1.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.2 | -9.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.5 | -16.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -15.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -6.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -0.3 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.9 | -1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | establishment of sister chromatid cohesion N-acetyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:21,529,284-21,600,884 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ESO1, EFO1, KIAA1911 |
| Gene groups (HGNC) | Lysine acetyltransferases |
| Reactome | 4 pathways, smallest: Establishment of Sister Chromatid Cohesion; S Phase; Cell Cycle, Mitotic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5FWF5](https://www.uniprot.org/uniprotkb/Q5FWF5) (N-acetyltransferase ESCO1):

> Acetyltransferase required for the establishment of sister chromatid cohesion. Couples the processes of cohesion and DNA replication to ensure that only sister chromatids become paired together. In contrast to the structural cohesins, the deposition and establishment factors are required only during S phase. Acts by mediating the acetylation of cohesin component SMC3.

**Summary**, from NCBI Gene [114799](https://www.ncbi.nlm.nih.gov/gene/114799):

> Enables identical protein binding activity; protein-lysine-acetyltransferase activity; and zinc ion binding activity. Involved in peptidyl-lysine acetylation; post-translational protein acetylation; and regulation of DNA replication. Located in chromatin. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24645](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24645) · Entrez [114799](https://www.ncbi.nlm.nih.gov/gene/114799) · UniProt [Q5FWF5](https://www.uniprot.org/uniprotkb/Q5FWF5) · Ensembl [ENSG00000141446](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141446)

## Data

Gene col 6520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6520); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6520, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6520]; `tensor/DDL_lfc|DDL_z.npy` [6520]; `embed/gene_vectors.npy` [6520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6520 or target_col == 6520). Every well: [[ESCO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESCO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
