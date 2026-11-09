---
symbol: "ACP1"
type: "gene"
col: 6791
ensembl_id: "ENSG00000143727"
name: "acid phosphatase 1"
location: "2p25.3"
module: 65
arm: "+"
pooled_cpm: 57.71
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# ACP1

*acid phosphatase 1* — 2p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.41× (z +13.6, q 2e-39, up in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.36× (z +4.7, q 2e-04, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.805× (z -4.7, q 0.001, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.505×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.333×; ⚠ toxic; cell-cycle shift, explains ~36% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VAMP7]] (+0.68, fdr 7e-06), [[SKIC3]] (+0.67, fdr 2e-05), [[TSNAX]] (+0.67, fdr 7e-06); moves opposite to [[PKNOX1]] (-0.59, fdr 4e-05), [[NOP56]] (-0.58, fdr 2e-05), [[ARMC5]] (-0.56, fdr 7e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +13.6 | 2e-39 | 46/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +12.4 | 7e-33 | 40/42 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +8.6 | 1e-15 | 40/45 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.40×** | +5.2 | 3e-05 | 32/47 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +4.7 | 2e-04 | 30/48 (NCI-H23, HT-29, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.33×** | +4.2 | 0.003 | 27/47 (NCI-H1573, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.009 | 24/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.073 | 22/48 (PANC-1, NCI-H23, …) | two highest doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.093 | 6/49 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.22× | +3.1 | 0.10 | 15/48 (Panc 03.27, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.22× | +3.1 | 0.10 | 21/48 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6791.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.505×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.333×; ⚠ toxic; cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.805×** | -4.7 | 0.001 | 24/48 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.801× | -3.4 | 0.18 | 20/48 (HepG2/C3A, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.815× | -3.2 | 0.30 | 19/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 73.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.94× (z +13.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 48.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 73.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +12.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 62.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 60.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +11.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 51.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 63.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +10.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 53.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 64.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 58.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +13.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 54.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 68.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +13.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.333× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[H4 (line)]] | wt | 45.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 90.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +9.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 92.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 65.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 47.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 31.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 61.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +9.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 58.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 44.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 47.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 85.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAMP7]] | +0.68 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[SKIC3]] | +0.67 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[TSNAX]] | +0.67 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[LONP2]] | +0.66 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[MRS2]] | +0.63 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[PRRC1]] | +0.62 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[ATP5F1C]] | +0.62 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[MIGA1]] | +0.62 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[EIF2AK1]] | +0.61 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ADH5]] | +0.61 | +0.65 / +0.39 | both halves | 6e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[RTRAF]] | +0.61 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[CLINT1]] | +0.61 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKNOX1]] | -0.59 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[NOP56]] | -0.58 | -0.52 / -0.47 | both halves | 2e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[ARMC5]] | -0.56 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[ZCCHC3]] | -0.56 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[TNPO2]] | -0.56 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[RELB]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TET3]] | -0.54 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[AP5S1]] | -0.54 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[RFX1]] | -0.54 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[SEMA4C]] | -0.53 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[SATB2]] | -0.53 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[SIK3]] | -0.53 | -0.49 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.4, -10.6); signed map (-31.7, -14.3). **Vector** length 68.1, 15.4% of its response variance represented; |z| ≥ 3 in 603 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +13.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +1.7 | +3.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +3.3 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.4 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.4 | -0.9 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | -0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.8 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | -0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | +0.7 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.4 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | acid phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.3 — chr2:264,140-278,283 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HAAP, LMW-PTP, LMWPTP |
| Gene groups (HGNC) | Class II Cys-based phosphatases; Acid phosphatases |
| Hallmark sets | XENOBIOTIC_METABOLISM, MYC_TARGETS_V1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P24666](https://www.uniprot.org/uniprotkb/P24666) (Low molecular weight phosphotyrosine protein phosphatase):

> Acts on tyrosine phosphorylated proteins, low-MW aryl phosphates and natural and synthetic acyl phosphates with differences in substrate specificity between isoform 1 and isoform 2.; [Isoform 3]: Does not possess phosphatase activity.

**Summary**, from NCBI Gene [52](https://www.ncbi.nlm.nih.gov/gene/52):

> The product of this gene belongs to the phosphotyrosine protein phosphatase family of proteins. It functions as an acid phosphatase and a protein tyrosine phosphatase by hydrolyzing protein tyrosine phosphate to protein tyrosine and orthophosphate. This enzyme also hydrolyzes orthophosphoric monoesters to alcohol and orthophosphate. This gene is genetically polymorphic, and three common alleles segregating at the corresponding locus give rise to six phenotypes. Each allele appears to encode at …

**Accessions** — [HGNC:122](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:122) · Entrez [52](https://www.ncbi.nlm.nih.gov/gene/52) · UniProt [P24666](https://www.uniprot.org/uniprotkb/P24666) · Ensembl [ENSG00000143727](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143727)

## Data

Gene col 6791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6791); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6791]; `tensor/DDL_lfc|DDL_z.npy` [6791]; `embed/gene_vectors.npy` [6791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6791 or target_col == 6791). Every well: [[ACP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
