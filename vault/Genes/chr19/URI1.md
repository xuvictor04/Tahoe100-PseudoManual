---
symbol: "URI1"
type: "gene"
col: 2555
ensembl_id: "ENSG00000105176"
name: "URI1 prefoldin like chaperone"
location: "19q12"
module: 40
arm: "+"
pooled_cpm: 144.8
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# URI1

*URI1 prefoldin like chaperone* — 19q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.25× (z +5.9, q 3e-06, up in 25 of 47 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 3.01×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H460 1.84×; ⚠ toxic); [[PH-797804 (drug)]] 5 µM in 1 line (C32 4.63×).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.301× (z -46.8, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP18]] (+0.72, fdr 7e-06), [[WRN]] (+0.71, fdr 7e-06), [[WDR3]] (+0.69, fdr 7e-06); moves opposite to [[BAZ2B]] (-0.64, fdr 2e-05), [[PNRC2]] (-0.63, fdr 1e-05), [[ZBED5]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2555.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 3.01×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H460 1.84×; ⚠ toxic); [[PH-797804 (drug)]] 5 µM in 1 line (C32 4.63×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +5.9 | 3e-06 | 25/47 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.18× | +4.3 | 0.005 | 19/48 (HEC-1-A, NCI-H23, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.2 | 0.23 | 5/49 (A-427, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2555.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.301×** | -46.8 | 0e+00 | 47/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.309×** | -31.1 | 0e+00 | 48/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.467×** | -19.6 | 0e+00 | 41/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.508×** | -18.7 | 0e+00 | 43/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.564×** | -15.8 | 0e+00 | 40/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -13.4 | 9e-39 | 36/49 (A549, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.649×** | -11.9 | 9e-31 | 36/48 (HOP62, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.706×** | -9.2 | 3e-18 | 33/47 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.805×** | -8.4 | 2e-15 | 29/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.755×** | -7.7 | 6e-13 | 29/48 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.779×** | -6.8 | 4e-10 | 27/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.787×** | -6.6 | 3e-09 | 28/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.790×** | -6.5 | 5e-09 | 29/48 (SW1417, A-172, …) | all doses, flat | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.789×** | -6.3 | 2e-08 | 30/48 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.804×** | -6.0 | 9e-08 | 27/48 (HOP62, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.818×** | -5.5 | 1e-06 | 27/48 (SW48, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.831×** | -4.8 | 5e-05 | 23/48 (SW48, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.841× | -4.7 | 6e-05 | 22/48 (LS 180, LoVo, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.850× | -4.3 | 5e-04 | 20/47 (C-33 A, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.899× | -4.1 | 9e-04 | 11/48 (LS 180, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.885× | -3.1 | 0.040 | 15/47 (HS-578T, A-172, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2555. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 214 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -43.3) |
| [[A-172 (line)]] | wt | 132 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -39.4) |
| [[HEC-1-A (line)]] | alt | 193 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -27.1) |
| [[SW48 (line)]] | wt | 171 | 1 | 8 | [[TAK-901 (drug)]] 0.05 µM 3.01× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -24.1) |
| [[HS-578T (line)]] | alt | 188 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -29.5) |
| [[A549 (line)]] | wt | 316 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -26.5) |
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -30.5) |
| [[NCI-H460 (line)]] | wt | 103 | 1 (1 ⚠) | 6 | [[Niclosamide (olamine) (drug)]] 5 µM 1.84× (z +9.6) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -28.8) |
| [[SNU-1 (line)]] | wt | 140 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.147× (z -20.1) |
| [[A498 (line)]] | wt | 211 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -38.2) |
| [[BT-474 (line)]] | alt | 99.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -14.1) |
| [[hTERT-HPNE (line)]] | wt | 108 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -27.7) |
| [[J82 (line)]] | alt | 140 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -27.8) |
| [[KATO III (line)]] | alt | 150 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -22.8) |
| [[MIA PaCa-2 (line)]] | alt | 184 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -30.4) |
| [[SW1417 (line)]] | alt | 132 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -24.1) |
| [[SW480 (line)]] | alt | 142 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -41.7) |
| [[C32 (line)]] | wt | 85.6 | 1 | 4 | [[PH-797804 (drug)]] 5 µM 4.63× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -20.2) |
| [[H4 (line)]] | wt | 248 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -14.3) |
| [[LoVo (line)]] | wt | 139 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -32.4) |
| [[LS 180 (line)]] | wt | 145 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -24.0) |
| [[NCI-H23 (line)]] | alt | 170 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -25.2) |
| [[PANC-1 (line)]] | alt | 210 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -36.1) |
| [[A-427 (line)]] | wt | 127 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -19.7) |
| [[AsPC-1 (line)]] | alt | 120 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -29.6) |
| [[NCI-H1573 (line)]] | alt | 56.4 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.167× (z -18.0) |
| [[RKO (line)]] | wt | 156 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -17.5) |
| [[RPMI-7951 (line)]] | alt | 150 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -26.0) |
| [[SW 900 (line)]] | alt | 108 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -15.7) |
| [[NCI-H2030 (line)]] | alt | 92.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -21.8) |
| [[SK-MEL-2 (line)]] | alt | 146 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -24.8) |
| [[AN3 CA (line)]] | alt | 145 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0872× (z -19.1) |
| [[CFPAC-1 (line)]] | alt | 80.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -19.8) |
| [[CHP-212 (line)]] | wt | 119 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.0) |
| [[COLO 205 (line)]] | alt | 96.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.193× (z -16.9) |
| [[HCT15 (line)]] | alt | 149 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -13.6) |
| [[Hs 766T (line)]] | wt | 106 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -22.7) |
| [[HT-29 (line)]] | alt | 128 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -24.2) |
| [[LOX-IMVI (line)]] | wt | 117 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -29.0) |
| [[NCI-H1792 (line)]] | alt | 124 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -18.4) |
| [[Panc 03.27 (line)]] | alt | 130 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -23.8) |
| [[SNU-423 (line)]] | alt | 94.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -34.0) |
| [[C-33 A (line)]] | alt | 143 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 81.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -13.7) |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 367 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2555), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP18]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[WRN]] | +0.71 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[WDR3]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[SHQ1]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[TAF5L]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[ANAPC5]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[IQCB1]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[TFB2M]] | +0.64 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[TMEM243]] | +0.64 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[SFXN2]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[DCAF13]] | +0.64 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[FAR1]] | +0.64 | +0.67 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.64 | -0.71 / -0.48 | both halves | 2e-05 |  |
| [[PNRC2]] | -0.63 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[ZBED5]] | -0.59 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[ZNF764]] | -0.58 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[ZNF827]] | -0.56 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[TIA1]] | -0.56 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[SLC9A8]] | -0.56 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[PATL2]] | -0.56 | -0.63 / -0.38 | both halves | 6e-05 |  |
| [[TET2]] | -0.55 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[TRIM69]] | -0.55 | -0.61 / -0.40 | both halves | 4e-05 |  |
| [[MAD2L1BP]] | -0.55 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[CASC9]] | -0.54 | -0.51 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises URI1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ARRDC4]] | B | ARRDC4 activity lowers URI1's level | lines that do not express ARRDC4 (8) vs lines expressing it (42) | 1.46× higher at baseline in the lines without ARRDC4 | 0.070 | ⚠ within organs, on part of the lines; also absent: C2orf72, ADAP1, BACH2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-3.6, -28.5); signed map (-43.4, -18.1). **Vector** length 125, 40.8% of its response variance represented; |z| ≥ 3 in 1,210 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +8.7 | +5.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +5.8 | -5.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +5.4 | -6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +4.6 | -7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.4 | +2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +0.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.9 | -18.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.0 | -31.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.9 | -6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -46.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.3 | -4.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | URI1 prefoldin like chaperone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q12 — chr19:29,923,644-30,016,612 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RMP, NNX3, FLJ10575, URI, PPP1R19; previously C19orf2 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Prefoldin subunits; Prefoldin-like complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O94763](https://www.uniprot.org/uniprotkb/O94763) (Unconventional prefoldin RPB5 interactor 1):

> Involved in gene transcription regulation. Acts as a transcriptional repressor in concert with the corepressor UXT to regulate androgen receptor (AR) transcription. May act as a tumor suppressor to repress AR-mediated gene transcription and to inhibit anchorage-independent growth in prostate cancer cells. Required for cell survival in ovarian cancer cells. Together with UXT, associates with chromatin to the NKX3-1 promoter region. Antagonizes transcriptional modulation via hepatitis B virus X …

**Summary**, from NCBI Gene [8725](https://www.ncbi.nlm.nih.gov/gene/8725):

> This gene encodes member of the prefoldin family of molecular chaperones. The encoded protein functions as a scaffolding protein and plays roles in ubiquitination and transcription, in part though interactions with the RNA polymerase II subunit RPB5. This gene may play a role in multiple malignancies including ovarian cancer and hepatocellular carcinoma. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene, and a pseudogene of this gene is …

**Accessions** — [HGNC:13236](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13236) · Entrez [8725](https://www.ncbi.nlm.nih.gov/gene/8725) · UniProt [O94763](https://www.uniprot.org/uniprotkb/O94763) · Ensembl [ENSG00000105176](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105176)

## Data

Gene col 2555: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2555); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2555, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2555]; `tensor/DDL_lfc|DDL_z.npy` [2555]; `embed/gene_vectors.npy` [2555]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2555 or target_col == 2555). Every well: [[URI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/URI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
