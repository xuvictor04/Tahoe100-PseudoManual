---
symbol: "GRIN2D"
type: "gene"
col: 2607
ensembl_id: "ENSG00000105464"
name: "glutamate ionotropic receptor NMDA type subunit 2D"
location: "19q13.33"
module: 160
arm: "+"
pooled_cpm: 23.03
n_lines_expressing: 30
n_dd_up: 4
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# GRIN2D

*glutamate ionotropic receptor NMDA type subunit 2D* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 1.50× (z +5.5, q 2e-05, up in 19 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.445× (z -15.5, q 0e+00, down in 23 of 28 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.363× (z -13.7, q 2e-40, down in 26 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FA2H]] (+0.60, fdr 1e-05), [[GIPR]] (+0.60, fdr 1e-05), [[BAHD1]] (+0.59, fdr 3e-05); moves opposite to [[ZMYND11]] (-0.63, fdr 9e-06), [[DIS3L]] (-0.59, fdr 2e-05), [[DPY19L1P2]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MBNL3]] → it (grade B ⚠); 6 go from it, the strongest it → [[ARHGEF18]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2607.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +5.5 | 2e-05 | 19/27 (HT-29, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.7 | 6e-04 | 11/28 (HEC-1-A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.065 | 14/28 (Panc 03.27, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.095 | 11/28 (LoVo, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 1.25× | +3.1 | 0.25 | 9/28 (NCI-H23, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2607.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.445×** | -15.5 | 0e+00 | 23/28 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.363×** | -13.7 | 2e-40 | 26/28 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.430×** | -11.4 | 5e-28 | 22/26 (KATO III, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -9.2 | 4e-18 | 24/28 (NCI-H1792, LS 180, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.497×** | -8.7 | 3e-16 | 22/24 (NCI-H23, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.524×** | -8.4 | 4e-15 | 21/28 (LoVo, COLO 205, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.532×** | -8.2 | 2e-14 | 20/27 (NCI-H23, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.581×** | -7.3 | 1e-11 | 21/28 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.580×** | -7.1 | 8e-11 | 17/21 (LoVo, Panc 03.27, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.628×** | -6.3 | 2e-08 | 21/28 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.624×** | -6.1 | 4e-08 | 19/27 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.644×** | -5.9 | 1e-07 | 17/28 (LOX-IMVI, NCI-H1792, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.635×** | -5.9 | 2e-07 | 19/28 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.468×** | -5.4 | 3e-06 | 21/28 (CFPAC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.742×** | -4.0 | 0.002 | 16/28 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -3.5 | 0.017 | 16/27 (Panc 03.27, SW 900, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.801×** | -3.0 | 0.085 | 11/28 (LOX-IMVI, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2607. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 39.5 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.235× (z -9.3) |
| [[LoVo (line)]] | wt | 51.8 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -26.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 62.0 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -15.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -12.0) |
| [[KATO III (line)]] | alt | 71.2 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -26.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 87.9 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -14.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 77.8 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -17.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 69.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -17.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 53.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -11.2) |
| [[HT-29 (line)]] | alt | 47.2 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -17.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LS 180 (line)]] | wt | 33.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 35.6 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.179× (z -12.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -10.7) |
| [[RKO (line)]] | wt | 51.0 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.127× (z -15.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -10.3) |
| [[A549 (line)]] | wt | 36.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -13.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0796× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -9.0) |
| [[A498 (line)]] | wt | 41.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[CFPAC-1 (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -18.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -9.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 9.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0848× (z -11.9) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -9.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.71 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.68 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.34 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.81 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2607), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FA2H]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[GIPR]] | +0.60 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[BAHD1]] | +0.59 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[LMTK3]] | +0.59 | +0.62 / +0.43 | both halves | 3e-05 | ⚠ same locus (40.3 kb: neighbours can correlate without regulation) |
| [[RAB43]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[LYPD3]] | +0.56 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[SWI5]] | +0.56 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[ZCCHC17]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[TMEM184B]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SLC8B1]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[RAD9A]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[TMEM92]] | +0.54 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[QPCTL]] | +0.54 | +0.46 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | -0.63 | -0.63 / -0.57 | both halves | 9e-06 |  |
| [[DIS3L]] | -0.59 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[DPY19L1P2]] | -0.58 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ZC3H14]] | -0.56 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[NT5DC1]] | -0.56 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ZNF280D]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[AASDHPPT]] | -0.55 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[ZNF236]] | -0.55 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[SENP6]] | -0.54 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[NELFCD]] | -0.54 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[USP24]] | -0.54 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[NHLRC2]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MBNL3]] | B | MBNL3 activity raises GRIN2D's level | lines that do not express MBNL3 (16) vs lines expressing it (34) | 2.39× lower at baseline in the lines without MBNL3 | 0.092 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[PRSS3]] | C | PRSS3 activity raises GRIN2D's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 3.46× lower at baseline in the lines without PRSS3 | 0.077 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF18]] | B | GRIN2D activity raises ARHGEF18's level | lines that do not express GRIN2D (20) vs lines expressing it (30) | 1.38× lower at baseline in the lines without GRIN2D | 0.037 | ⚠ within organs, on part of the lines; also absent: MUC3A, TMEM139, RASSF6 |
| [[CRYBG2]] | B | GRIN2D activity raises CRYBG2's level | lines that do not express GRIN2D (20) vs lines expressing it (30) | 2.90× lower at baseline in the lines without GRIN2D | 0.054 | ⚠ within organs, on part of the lines; also absent: MUC3A, TMEM139, RASSF6 |
| [[MCCC2]] | B | GRIN2D activity lowers MCCC2's level | lines that do not express GRIN2D (20) vs lines expressing it (30) | 1.19× higher at baseline in the lines without GRIN2D | 0.084 | ⚠ within organs, on part of the lines; also absent: MUC3A, TMEM139, RASSF6 |
| [[ZC3H14]] | B | GRIN2D activity lowers ZC3H14's level | lines that do not express GRIN2D (20) vs lines expressing it (30) | 1.16× higher at baseline in the lines without GRIN2D | 0.089 | ⚠ within organs, on part of the lines; also absent: MUC3A, TMEM139, RASSF6 |
| [[LMTK3]] | B | GRIN2D activity raises LMTK3's level | lines that do not express GRIN2D (20) vs lines expressing it (30) | 2.43× lower at baseline in the lines without GRIN2D | 0.089 | ⚠ within organs, on part of the lines; also absent: MUC3A, TMEM139, RASSF6 |
| [[PRSS3]] | C | GRIN2D activity raises PRSS3's level | lines that do not express GRIN2D (20) vs lines expressing it (30) | 3.16× lower at baseline in the lines without GRIN2D | 0.079 | ⚠ within organs, on part of the lines; also absent: MUC3A, TMEM139, RASSF6; co-absent with the target |

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (8.9, 2.0); signed map (-24.5, 22.8). **Vector** length 83.7, 23.2% of its response variance represented; |z| ≥ 3 in 665 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +4.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.1 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +1.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.2 | +2.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +1.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -13.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.4 | -15.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | glutamate ionotropic receptor NMDA type subunit 2D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,393,668-48,444,931 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GluN2D, EB11, NR2D; previously NMDAR2D |
| Gene groups (HGNC) | Glutamate ionotropic receptor NMDA type subunits |
| Reactome | 17 pathways, smallest: Ras activation upon Ca2+ influx through NMDA receptor; Synaptic adhesion-like molecules; Unblocking of NMDA receptors, glutamate binding and activation |
| Matched by | ensembl_id |

**Function**, from UniProt [O15399](https://www.uniprot.org/uniprotkb/O15399) (Glutamate receptor ionotropic, NMDA 2D):

> Component of N-methyl-D-aspartate (NMDA) receptors (NMDARs) that function as heterotetrameric, ligand-gated cation channels with high calcium permeability and voltage-dependent block by Mg(2+). Participates in synaptic plasticity for learning and memory formation (By similarity). Channel activation requires binding of the neurotransmitter L-glutamate to the GluN2 subunit, glycine or D-serine binding to the GluN1 subunit, plus membrane depolarization to eliminate channel inhibition by Mg(2+). …

**Summary**, from NCBI Gene [2906](https://www.ncbi.nlm.nih.gov/gene/2906):

> N-methyl-D-aspartate (NMDA) receptors are a class of ionotropic glutamate receptors. NMDA channel has been shown to be involved in long-term potentiation, an activity-dependent increase in the efficiency of synaptic transmission thought to underlie certain kinds of memory and learning. NMDA receptor channels are heteromers composed of the key receptor subunit NMDAR1 (GRIN1) and 1 or more of the 4 NMDAR2 subunits: NMDAR2A (GRIN2A), NMDAR2B (GRIN2B), NMDAR2C (GRIN2C), and NMDAR2D (GRIN2D). …

**Accessions** — [HGNC:4588](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4588) · Entrez [2906](https://www.ncbi.nlm.nih.gov/gene/2906) · UniProt [O15399](https://www.uniprot.org/uniprotkb/O15399) · Ensembl [ENSG00000105464](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105464)

## Data

Gene col 2607: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2607); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2607, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2607]; `tensor/DDL_lfc|DDL_z.npy` [2607]; `embed/gene_vectors.npy` [2607]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2607 or target_col == 2607). Every well: [[GRIN2D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRIN2D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
