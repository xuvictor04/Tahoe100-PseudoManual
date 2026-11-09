---
symbol: "SNRPD3"
type: "gene"
col: 1846
ensembl_id: "ENSG00000100028"
name: "small nuclear ribonucleoprotein D3 polypeptide"
location: "22q11.23"
module: 36
arm: "+"
pooled_cpm: 49.2
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# SNRPD3

*small nuclear ribonucleoprotein D3 polypeptide* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.11× (z +13.8, q 2e-40, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +11.9, q 1e-30, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.189×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2L3]] (+0.68, fdr 1e-05), [[RBM14-RBM4]] (+0.66, fdr 7e-06), [[ANAPC10]] (+0.63, fdr 3e-05); moves opposite to [[ZC3H6]] (-0.62, fdr 1e-05), [[GATAD1]] (-0.55, fdr 4e-05), [[PIM3]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1846.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.11×** | +13.8 | 2e-40 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.07×** | +13.4 | 1e-38 | 44/47 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.11×** | +13.3 | 7e-38 | 36/42 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.92×** | +12.0 | 3e-31 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +11.9 | 1e-30 | 47/48 (SW480, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.87×** | +11.5 | 1e-28 | 45/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +9.9 | 4e-21 | 45/48 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.49×** | +8.8 | 1e-16 | 41/49 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +8.6 | 4e-16 | 39/48 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.62×** | +8.2 | 1e-14 | 34/45 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +8.0 | 5e-14 | 43/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.50×** | +7.5 | 4e-12 | 40/48 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +7.2 | 2e-11 | 38/48 (COLO 205, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.38×** | +5.9 | 1e-07 | 27/48 (NCI-H1573, SW480, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.32×** | +5.1 | 1e-05 | 30/47 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.9 | 4e-05 | 20/48 (A-172, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.7 | 8e-05 | 23/48 (SW480, HT-29, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.019 | 18/47 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.021 | 15/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.040 | 14/48 (HOP62, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | 1.18× | +3.0 | 0.060 | 12/48 (HS-578T, SK-MEL-2, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.18× | +2.9 | 0.070 | 10/48 (NCI-H460, HS-578T, …) | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.17× | +2.8 | 0.088 | 8/48 (COLO 205, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1846.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.189×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.880× | -3.4 | 0.43 | 10/48 (PANC-1, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1846. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 64.2 | 6 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +12.7) | — |
| [[LoVo (line)]] | wt | 48.1 | 5 (4 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.61× (z +10.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.69× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 46.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 38.5 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.35× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 32.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[PANC-1 (line)]] | alt | 34.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.4) | — |
| [[A549 (line)]] | wt | 35.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.01× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[HEC-1-A (line)]] | alt | 73.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 62.3 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.42× (z +9.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 24.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 37.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1792 (line)]] | alt | 33.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 34.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +11.5) | — |
| [[A-172 (line)]] | wt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A-427 (line)]] | wt | 49.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.60× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[AsPC-1 (line)]] | alt | 33.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[C-33 A (line)]] | alt | 81.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[CFPAC-1 (line)]] | alt | 47.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[H4 (line)]] | wt | 35.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.76× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[Hs 766T (line)]] | wt | 49.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[HT-29 (line)]] | alt | 43.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[KATO III (line)]] | alt | 62.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H23 (line)]] | alt | 51.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[RKO (line)]] | wt | 63.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 65.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.59× (z +9.0) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW48 (line)]] | wt | 65.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A498 (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 78.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1846), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2L3]] | +0.68 | +0.76 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[RBM14-RBM4]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ANAPC10]] | +0.63 | +0.65 / +0.43 | both halves | 3e-05 | STRING 589 |
| [[PSMB3]] | +0.62 | +0.65 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 472 |
| [[STX16-NPEPL1]] | +0.62 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[CDC123]] | +0.61 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[HSF1]] | +0.60 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[POLR2B]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 559 |
| [[UBOX5]] | +0.58 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[SMIM7]] | +0.57 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[RNF121]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[OGFOD3]] | +0.56 | +0.55 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H6]] | -0.62 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[GATAD1]] | -0.55 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PIM3]] | -0.53 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[APLF]] | -0.52 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[GRINA]] | -0.50 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[HIVEP2]] | -0.50 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[NFKBIB]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 | pathway: Dengue Virus-Host Interactions |
| [[TRMT1L]] | -0.50 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[RPP25L]] | -0.49 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[COMMD3]] | -0.49 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[ATF3]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[TMEM42]] | -0.49 | -0.37 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-24.6, -10.9); signed map (-32.4, -30.4). **Vector** length 67.1, 14.3% of its response variance represented; |z| ≥ 3 in 1,066 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.9 | +9.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +8.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.0 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +8.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +4.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +1.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.5 | +1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.9 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.4 | -1.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.3 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -1.0 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein D3 polypeptide |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.23 — chr22:24,555,958-24,582,052 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SMD3, Sm-D3 |
| Gene groups (HGNC) | Sm spliceosomal proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 24 pathways, smallest: SLBP independent Processing of Histone Pre-mRNAs; SLBP Dependent Processing of Replication-Dependent Histone Pre-mRNAs; Processing of Capped Intronless Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P62318](https://www.uniprot.org/uniprotkb/P62318) (Small nuclear ribonucleoprotein Sm D3):

> Plays a role in pre-mRNA splicing as a core component of the spliceosomal U1, U2, U4 and U5 small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome. Component of both the pre-catalytic spliceosome B complex and activated spliceosome C complexes. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs. As part of the U7 snRNP it is involved in histone pre-mRNA 3'-end processing (By similarity).

**Summary**, from NCBI Gene [6634](https://www.ncbi.nlm.nih.gov/gene/6634):

> This gene encodes a core component of the spliceosome, which is a nuclear ribonucleoprotein complex that functions in pre-mRNA splicing. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:11160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11160) · Entrez [6634](https://www.ncbi.nlm.nih.gov/gene/6634) · UniProt [P62318](https://www.uniprot.org/uniprotkb/P62318) · Ensembl [ENSG00000100028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100028)

## Data

Gene col 1846: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1846); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1846, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1846]; `tensor/DDL_lfc|DDL_z.npy` [1846]; `embed/gene_vectors.npy` [1846]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1846 or target_col == 1846). Every well: [[SNRPD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRPD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
