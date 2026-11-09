---
symbol: "KNOP1"
type: "gene"
col: 2384
ensembl_id: "ENSG00000103550"
name: "lysine rich nucleolar protein 1"
location: "16p12.3"
module: 36
arm: "+"
pooled_cpm: 43.85
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# KNOP1

*lysine rich nucleolar protein 1* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.52× (z +9.4, q 3e-18, up in 34 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.27× (z +3.5, q 0.036, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A498 10.8×, HEC-1-A 9.81×, SW 900 35.2×, LoVo 9.64×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A498 8.47×, SW 900 28.0×, HEC-1-A 4.84×, SHP-77 4.96×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW 900 18.6×, A498 5.59×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.473× (z -10.8, q 3e-24, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGU]] (+0.70, fdr 7e-06), [[DHX57]] (+0.67, fdr 1e-05), [[CTU1]] (+0.64, fdr 7e-06); moves opposite to [[CGGBP1]] (-0.64, fdr 3e-05), [[SGO1-AS1]] (-0.59, fdr 3e-05), [[TAF9B]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2384.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A498 10.8×, HEC-1-A 9.81×, SW 900 35.2×, LoVo 9.64×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A498 8.47×, SW 900 28.0×, HEC-1-A 4.84×, SHP-77 4.96×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW 900 18.6×, A498 5.59×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.52×** | +9.4 | 3e-18 | 34/44 (A498, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.12×** | +7.4 | 5e-11 | 29/42 (A498, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.7 | 2e-06 | 35/46 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.78×** | +5.5 | 6e-06 | 29/43 (SW 900, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.62×** | +4.9 | 1e-04 | 32/48 (COLO 205, NCI-H1573, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.48×** | +4.0 | 0.006 | 27/48 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.44×** | +3.7 | 0.017 | 26/48 (AsPC-1, NCI-H1573, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.036 | 26/48 (A549, NCI-H1573, …) | rises with dose |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.071 | 21/48 (HS-578T, KATO III, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +3.2 | 0.071 | 19/48 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.36×** | +3.2 | 0.071 | 22/46 (SW 900, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.36×** | +3.2 | 0.071 | 21/47 (LoVo, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2384.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.473×** | -10.8 | 3e-24 | 39/48 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.661×** | -4.1 | 0.014 | 27/48 (AN3 CA, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.477×** | -3.9 | 0.015 | 28/48 (Hs 766T, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.708×** | -3.5 | 0.065 | 29/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.794× | -3.3 | 0.11 | 28/48 (SNU-1, A498, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.733× | -3.2 | 0.14 | 20/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.716× | -3.1 | 0.14 | 20/48 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2384. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 47.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.8× (z +17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HEC-1-A (line)]] | alt | 35.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.81× (z +16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HOP62 (line)]] | alt | 41.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -12.7) |
| [[LoVo (line)]] | wt | 16.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.64× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[Panc 03.27 (line)]] | alt | 23.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.94× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SW 900 (line)]] | alt | 16.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 35.2× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[BT-474 (line)]] | alt | 47.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 4.96× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -9.2) |
| [[C32 (line)]] | wt | 32.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -15.6) |
| [[NCI-H460 (line)]] | wt | 28.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -10.2) |
| [[PANC-1 (line)]] | alt | 180 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -13.5) |
| [[SHP-77 (line)]] | alt | 36.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Dinaciclib (drug)]] 5 µM 0.253× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-427 (line)]] | wt | 49.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -8.5) |
| [[AN3 CA (line)]] | alt | 59.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.129× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 14.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.95× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[H4 (line)]] | wt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.12× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HCT15 (line)]] | alt | 47.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HepG2_C3A (line)]] | wt | 31.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.3) |
| [[Hs 766T (line)]] | wt | 60.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.7) |
| [[HS-578T (line)]] | alt | 44.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -10.7) |
| [[J82 (line)]] | alt | 44.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.10× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[KATO III (line)]] | alt | 62.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 42.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 43.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -11.2) |
| [[RKO (line)]] | wt | 35.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 28.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 55.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -12.2) |
| [[SW1417 (line)]] | alt | 41.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -9.0) |
| [[SW480 (line)]] | alt | 38.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -9.4) |
| [[A-172 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2384), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGU]] | +0.70 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[DHX57]] | +0.67 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[CTU1]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[HERC2P9]] | +0.64 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ZNF692]] | +0.64 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[NARS2]] | +0.63 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ANKS6]] | +0.63 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CHCHD6]] | +0.63 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[WRN]] | +0.63 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ZNF496]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[GTF2H2]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TYW1]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGGBP1]] | -0.64 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[SGO1-AS1]] | -0.59 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[TAF9B]] | -0.58 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[UBE2A]] | -0.58 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[FAM120AOS]] | -0.57 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[RAP2C]] | -0.57 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TSGA10]] | -0.57 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[MALINC1]] | -0.56 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[SPDYA]] | -0.56 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ABCA10]] | -0.55 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[ARMT1]] | -0.55 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[PRKAR1A]] | -0.55 | -0.49 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.634). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-8.4, -19.0); signed map (-41.7, -19.5). **Vector** length 82.8, 22.7% of its response variance represented; |z| ≥ 3 in 646 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +3.1 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.9 | -10.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -3.5 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | lysine rich nucleolar protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:19,701,937-19,718,235 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 101F10.1, FAM191A, TSG118; previously C16orf88 |
| Matched by | ensembl_id |

UniProt [Q1ED39](https://www.uniprot.org/uniprotkb/Q1ED39) carries no function annotation.

**Summary**, from NCBI Gene [400506](https://www.ncbi.nlm.nih.gov/gene/400506):

> The protein encoded by this gene is a nucleolar protein that interacts with zinc finger 106 protein. The encoded protein has several of the same characteristics as nucleostemin and may be involved in testis development. [provided by RefSeq, Feb 2017]

**Accessions** — [HGNC:34404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34404) · Entrez [400506](https://www.ncbi.nlm.nih.gov/gene/400506) · UniProt [Q1ED39](https://www.uniprot.org/uniprotkb/Q1ED39) · Ensembl [ENSG00000103550](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103550)

## Data

Gene col 2384: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2384); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2384, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2384]; `tensor/DDL_lfc|DDL_z.npy` [2384]; `embed/gene_vectors.npy` [2384]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2384 or target_col == 2384). Every well: [[KNOP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KNOP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
