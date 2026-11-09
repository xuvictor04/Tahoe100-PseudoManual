---
symbol: "MTHFD2L"
type: "gene"
col: 8768
ensembl_id: "ENSG00000163738"
name: "methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 2 like"
location: "4q13.3"
module: 4
arm: "+"
pooled_cpm: 65.82
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MTHFD2L

*methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 2 like* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.77× (z +10.1, q 3e-21, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Radotinib (drug)]] 5 µM: 0.828× (z -5.1, q 2e-04, down in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.388×, NCI-H460 0.437×, HepG2/C3A 0.364×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.363×, NCI-H460 0.556×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.209×, A-427 0.445×; ⚠ toxic; transcription drop); [[Fulvestrant (drug)]] 5 µM in 1 line (NCI-H596 0.176×); [[Trametinib (drug)]] 0.5 µM in 1 line (NCI-H460 0.500×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BICD1]] (+0.64, fdr 7e-06), [[TANGO6]] (+0.62, fdr 1e-05), [[GNL3L]] (+0.61, fdr 1e-05); moves opposite to [[APAF1]] (-0.68, fdr 7e-06), [[HCFC1R1]] (-0.59, fdr 1e-05), [[IDH2]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8768.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.77×** | +10.1 | 3e-21 | 40/47 (LOX-IMVI, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +10.0 | 5e-21 | 34/46 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +9.9 | 5e-21 | 35/47 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +9.3 | 2e-18 | 35/46 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +9.2 | 5e-18 | 31/47 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +9.0 | 3e-17 | 35/46 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +8.9 | 5e-17 | 31/47 (LOX-IMVI, COLO 205, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +8.2 | 2e-14 | 37/47 (LOX-IMVI, COLO 205, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +8.2 | 2e-14 | 31/47 (C32, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +7.6 | 1e-12 | 34/44 (A549, LS 180, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +6.7 | 8e-10 | 24/47 (SW480, RKO, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +6.4 | 6e-09 | 28/47 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.43×** | +6.4 | 7e-09 | 26/46 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +5.9 | 1e-07 | 26/47 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.6 | 6e-07 | 25/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +5.2 | 6e-06 | 24/47 (LS 180, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +4.7 | 7e-05 | 24/47 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 9e-04 | 22/47 (LS 180, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +4.1 | 0.001 | 18/47 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8768.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.388×, NCI-H460 0.437×, HepG2/C3A 0.364×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.363×, NCI-H460 0.556×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.209×, A-427 0.445×; ⚠ toxic; transcription drop); [[Fulvestrant (drug)]] 5 µM in 1 line (NCI-H596 0.176×); [[Trametinib (drug)]] 0.5 µM in 1 line (NCI-H460 0.500×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.828×** | -5.1 | 2e-04 | 20/47 (RKO, NCI-H2030, …) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | 0.869× | -3.8 | 0.039 | 10/48 (NCI-H1792, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | **0.825×** | -3.7 | 0.045 | 22/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.848× | -3.6 | 0.050 | 14/47 (NCI-H460, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.702×** | -3.5 | 0.050 | 17/46 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.859× | -3.3 | 0.10 | 12/49 (NCI-H460, J82, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8768. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 156 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.500× (z -9.0) |
| [[HOP62 (line)]] | alt | 27.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +14.0) | — |
| [[LoVo (line)]] | wt | 58.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +16.1) | — |
| [[CFPAC-1 (line)]] | alt | 20.3 | 3 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.23× (z +9.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.55× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 38.6 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.77× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 62.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.47× (z +12.1) | — |
| [[RKO (line)]] | wt | 119 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 105 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -16.2) |
| [[Hs 766T (line)]] | wt | 21.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 35.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.02× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 97.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +12.0) | — |
| [[C-33 A (line)]] | alt | 64.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[C32 (line)]] | wt | 35.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.92× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +13.3) | — |
| [[HepG2_C3A (line)]] | wt | 73.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 90.0 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.48× (z +9.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 45.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.06× (z +9.8) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 82.5 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.89× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 92.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 70.9 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.176× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 56.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.41× (z +8.6) | — |
| [[A-172 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 50.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8768), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BICD1]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TANGO6]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[GNL3L]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ATE1]] | +0.61 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[DPH5-DT]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | +0.58 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[ABCE1]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[CLPB]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[LINC01355]] | +0.57 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[TRMT11]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[TPK1]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 | pathway: Metabolism of vitamins and cofactors |
| [[COMMD10]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APAF1]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[HCFC1R1]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[IDH2]] | -0.58 | -0.55 / -0.52 | both halves | 1e-05 | STRING 451 |
| [[MXI1]] | -0.58 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[MMUT]] | -0.57 | -0.51 / -0.55 | both halves | 1e-05 | pathway: Metabolism of vitamins and cofactors |
| [[MOSPD3]] | -0.57 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[ANG]] | -0.55 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[SPATA7]] | -0.55 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ARL3]] | -0.55 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[THAP8]] | -0.55 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[KMT5C]] | -0.54 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[RNASE4]] | -0.54 | -0.60 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EREG]] | B | EREG activity strengthens MTHFD2L's drug response | lines that do not express EREG (25) vs lines expressing it (22) | the lines without EREG respond 0.59× as strongly (z diff +1.60); strongest at Homoharringtonine 5 µM: 1.18x vs 1.64x (z diff +3.2) | 0.056 | ⚠ within organs, on part of the lines; also absent: DPP4, IL20RA, HS3ST1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.506). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.4, -31.0); signed map (6.0, -44.7). **Vector** length 121, 33.0% of its response variance represented; |z| ≥ 3 in 1,265 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.0 | +9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +8.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.9 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.9 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +8.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.2 | +4.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | -1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +0.6 |
|  | [[NG25 (drug)]] 5 µM |  | -4.0 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.7 | -3.6 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -2.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:74,114,174-74,303,099 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC72244 |
| Gene groups (HGNC) | MTHFD family; Methylenetetrahydrofolate dehydrogenases |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 3 pathways, smallest: Metabolism of folate and pterines; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H903](https://www.uniprot.org/uniprotkb/Q9H903) (Bifunctional methylenetetrahydrofolate dehydrogenase/cyclohydrolase 2, mitochondrial):

> Bifunctional mitochondrial folate-interconverting enzyme that has both NAD/NADP-dependent methylenetetrahydrofolate dehydrogenase and methenyltetrahydrofolate cyclohydrolase activities.

**Summary**, from NCBI Gene [441024](https://www.ncbi.nlm.nih.gov/gene/441024):

> Predicted to enable methenyltetrahydrofolate cyclohydrolase activity; methylenetetrahydrofolate dehydrogenase (NAD+) activity; and methylenetetrahydrofolate dehydrogenase (NADP+) activity. Predicted to be involved in tetrahydrofolate interconversion. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31865](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31865) · Entrez [441024](https://www.ncbi.nlm.nih.gov/gene/441024) · UniProt [Q9H903](https://www.uniprot.org/uniprotkb/Q9H903) · Ensembl [ENSG00000163738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163738)

## Data

Gene col 8768: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8768); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8768, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8768]; `tensor/DDL_lfc|DDL_z.npy` [8768]; `embed/gene_vectors.npy` [8768]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8768 or target_col == 8768). Every well: [[MTHFD2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTHFD2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
