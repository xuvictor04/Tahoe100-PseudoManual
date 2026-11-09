---
symbol: "CLTA"
type: "gene"
col: 4369
ensembl_id: "ENSG00000122705"
name: "clathrin light chain A"
location: "9p13.3"
module: 146
arm: "-"
pooled_cpm: 107.78
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# CLTA

*clathrin light chain A* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +12.5, q 2e-33, up in 45 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.204×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.518×; ⚠ cell-cycle shift, explains ~72% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB7A]] (+0.62, fdr 5e-05), [[WWP2]] (+0.58, fdr 1e-05), [[SNX8]] (+0.57, fdr 1e-05); moves opposite to [[SSX2IP]] (-0.51, fdr 2e-05), [[KCTD3]] (-0.49, fdr 3e-05), [[HSF2]] (-0.49, fdr 8e-05).
> It sits in the **-** arm of [[Module 146]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 23 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4369.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +12.5 | 2e-33 | 45/49 (A-172, AsPC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.76×** | +9.6 | 3e-19 | 41/49 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.62×** | +7.8 | 1e-12 | 30/44 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +7.6 | 4e-12 | 43/48 (PANC-1, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.54×** | +7.4 | 2e-11 | 40/48 (SW480, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.33×** | +6.8 | 1e-09 | 32/48 (NCI-H460, Hs 766T, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.55×** | +6.7 | 1e-09 | 36/45 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.48×** | +6.6 | 3e-09 | 39/48 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.46×** | +6.4 | 9e-09 | 37/48 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.44×** | +6.2 | 4e-08 | 36/48 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.44×** | +6.0 | 1e-07 | 35/48 (PANC-1, Hs 766T, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.41×** | +5.9 | 2e-07 | 33/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.7 | 5e-07 | 33/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.39×** | +5.6 | 1e-06 | 29/48 (PANC-1, Hs 766T, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.3 | 5e-04 | 31/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.1 | 0.001 | 18/48 (A-172, HOP62, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.006 | 25/47 (PANC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.037 | 19/48 (NCI-H23, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.20×** | +2.9 | 0.067 | 20/48 (HOP62, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.37×** | +2.9 | 0.077 | 13/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.37×** | +2.8 | 0.095 | 15/48 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +2.8 | 0.097 | 20/48 (NCI-H1792, HOP62, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4369.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.204×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.518×; ⚠ cell-cycle shift, explains ~72% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.844× | -4.1 | 0.023 | 18/48 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.867× | -3.4 | 0.20 | 12/48 (NCI-H23, A-427, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.818× | -3.2 | 0.20 | 24/50 (NCI-H23, NCI-H596, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.814× | -3.2 | 0.20 | 23/48 (NCI-H23, C-33 A, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.833× | -3.1 | 0.20 | 14/48 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4369. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 234 | 9 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +12.7) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.99× (z +10.7) | — |
| [[A498 (line)]] | wt | 133 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 73.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.1) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.0) | — |
| [[A-172 (line)]] | wt | 79.4 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +12.8) | — |
| [[HS-578T (line)]] | alt | 74.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 112 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.6) | — |
| [[SW480 (line)]] | alt | 124 | 3 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.16× (z +11.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.88× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 74.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 126 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.6) ⚠ cell-cycle shift, explains ~72% of this change | — |
| [[NCI-H2030 (line)]] | alt | 56.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 74.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.6) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +8.7) | — |
| [[A-427 (line)]] | wt | 84.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -10.5) ⚠ cell-cycle shift, explains ~72% of this change |
| [[A549 (line)]] | wt | 115 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 179 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +12.8) | — |
| [[C-33 A (line)]] | alt | 74.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[H4 (line)]] | wt | 95.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.5) ⚠ cell-cycle shift, explains ~72% of this change | — |
| [[LOX-IMVI (line)]] | wt | 108 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 64.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +11.7) | — |
| [[AN3 CA (line)]] | alt | 116 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 80.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 92.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 146 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 130 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 129 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 99.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4369), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB7A]] | +0.62 | +0.39 / +0.60 | both halves | 5e-05 | pathway: MHC class II antigen presentation |
| [[WWP2]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[SNX8]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ATP6V1D]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PLEKHM1]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[RNF103-CHMP3]] | +0.51 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CD63]] | +0.50 | +0.36 / +0.46 | both halves | 1e-04 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[BIN3]] | +0.50 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[CTNS]] | +0.49 | +0.60 / +0.37 | both halves | 8e-05 |  |
| [[GPATCH2L]] | +0.49 | +0.37 / +0.47 | both halves | 8e-05 |  |
| [[NSMCE2]] | +0.48 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[VAC14]] | +0.48 | +0.47 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSX2IP]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[KCTD3]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[HSF2]] | -0.49 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[KDM1A]] | -0.48 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[HOOK1]] | -0.48 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ARHGAP17]] | -0.47 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[RAD23B]] | -0.46 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[TADA1]] | -0.46 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[BLMH]] | -0.45 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[FBXO7]] | -0.45 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[PCCB]] | -0.45 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[HLTF]] | -0.44 | -0.43 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **-** arm (projection on the module's main direction -0.454). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-50.7, 12.1); signed map (7.0, 15.7). **Vector** length 71.4, 19.0% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.4 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +12.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.5 | +3.9 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +0.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.1 | +1.1 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +2.0 | +1.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | +2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -2.1 | +6.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.5 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | clathrin light chain A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:36,190,856-36,304,781 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Lca |
| Gene groups (HGNC) | Clathrin subunits |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 36 pathways, smallest: Entry of Influenza Virion into Host Cell via Endocytosis; Formation of annular gap junctions; Gap junction degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P09496](https://www.uniprot.org/uniprotkb/P09496) (Clathrin light chain A):

> Clathrin is the major protein of the polyhedral coat of coated pits and vesicles. Acts as a component of the TACC3/ch-TOG/clathrin complex proposed to contribute to stabilization of kinetochore fibers of the mitotic spindle by acting as inter-microtubule bridge.

**Summary**, from NCBI Gene [1211](https://www.ncbi.nlm.nih.gov/gene/1211):

> Clathrin is a large, soluble protein composed of heavy and light chains. It functions as the main structural component of the lattice-type cytoplasmic face of coated pits and vesicles which entrap specific macromolecules during receptor-mediated endocytosis. This gene encodes one of two clathrin light chain proteins which are believed to function as regulatory elements. Alternative splicing results in multiple transcript variants. Related pseudogenes have been identified on chromosomes 8 and …

**Accessions** — [HGNC:2090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2090) · Entrez [1211](https://www.ncbi.nlm.nih.gov/gene/1211) · UniProt [P09496](https://www.uniprot.org/uniprotkb/P09496) · Ensembl [ENSG00000122705](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122705)

## Data

Gene col 4369: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4369); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4369, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4369]; `tensor/DDL_lfc|DDL_z.npy` [4369]; `embed/gene_vectors.npy` [4369]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4369 or target_col == 4369). Every well: [[CLTA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLTA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
