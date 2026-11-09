---
symbol: "ARPC1B"
type: "gene"
col: 5065
ensembl_id: "ENSG00000130429"
name: "actin related protein 2/3 complex subunit 1B"
location: "7q22.1"
module: 136
arm: "+"
pooled_cpm: 134.94
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 7
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# ARPC1B

*actin related protein 2/3 complex subunit 1B* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.31× (z +10.2, q 8e-22, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H1792 8.07×, SW480 5.92×, SNU-1 12.8×, C32 6.17×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1792 6.33×, HCT15 6.68×, HEC-1-A 3.83×, NCI-H460 3.99×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.349× (z -13.1, q 1e-36, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3BGRL3]] (+0.61, fdr 1e-05), [[TMEM41B]] (+0.61, fdr 1e-05), [[RASA2]] (+0.60, fdr 1e-05); moves opposite to [[ZXDA]] (-0.61, fdr 1e-04), [[ZXDB]] (-0.61, fdr 3e-05), [[RBM7]] (-0.61, fdr 3e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5065.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H1792 8.07×, SW480 5.92×, SNU-1 12.8×, C32 6.17×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1792 6.33×, HCT15 6.68×, HEC-1-A 3.83×, NCI-H460 3.99×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.31×** | +10.2 | 8e-22 | 48/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.32×** | +10.2 | 8e-22 | 40/41 (NCI-H1792, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +7.5 | 1e-11 | 38/44 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.49×** | +3.5 | 0.062 | 30/47 (SW 900, A-172, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5065.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.349×** | -13.1 | 1e-36 | 45/46 (AsPC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.434×** | -7.4 | 5e-11 | 43/46 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.632×** | -5.7 | 2e-06 | 43/47 (AsPC-1, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.468×** | -3.5 | 0.055 | 33/48 (HOP62, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.642×** | -3.5 | 0.055 | 30/49 (NCI-H23, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.666×** | -3.4 | 0.055 | 29/47 (BT-474, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.490×** | -3.3 | 0.082 | 31/47 (RKO, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5065. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 69.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.99× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.5) |
| [[SW480 (line)]] | alt | 72.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -11.6) |
| [[HCT15 (line)]] | alt | 58.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 6.68× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -9.8) |
| [[HOP62 (line)]] | alt | 72.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -14.3) |
| [[Hs 766T (line)]] | wt | 149 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.69× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 122 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.69× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 47.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.33× (z +11.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 78.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -14.3) |
| [[A498 (line)]] | wt | 204 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 73.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 1,838 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -26.0) |
| [[C32 (line)]] | wt | 283 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.17× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 65.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +10.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 152 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -16.8) |
| [[LoVo (line)]] | wt | 38.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 62.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.59× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 104 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -14.3) |
| [[PANC-1 (line)]] | alt | 122 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -14.9) |
| [[RKO (line)]] | wt | 94.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -18.4) |
| [[A-427 (line)]] | wt | 136 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -20.1) |
| [[BT-474 (line)]] | alt | 55.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -14.6) |
| [[COLO 205 (line)]] | alt | 49.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.05× (z +8.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 66.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 76.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.0) |
| [[HT-29 (line)]] | alt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -14.4) |
| [[J82 (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.1) |
| [[LS 180 (line)]] | wt | 48.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 139 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -17.3) |
| [[NCI-H2347 (line)]] | alt | 86.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 216 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -11.2) |
| [[SNU-1 (line)]] | wt | 46.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.8× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 73.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -10.6) |
| [[SW 900 (line)]] | alt | 63.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -13.1) |
| [[SW1417 (line)]] | alt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -9.8) |
| [[SW48 (line)]] | wt | 80.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.0) |
| [[A-172 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.9 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 90.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5065), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3BGRL3]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[TMEM41B]] | +0.61 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[RASA2]] | +0.60 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[COX6A1]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[DNASE1L1]] | +0.59 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[FXYD5]] | +0.59 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[MYO9B]] | +0.58 | +0.61 / +0.50 | both halves | 1e-05 | pathway: FCGR3A-mediated phagocytosis; STRING 532 |
| [[STXBP1]] | +0.58 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[CORO7]] | +0.58 | +0.61 / +0.43 | both halves | 3e-05 | same gene group |
| [[WDFY2]] | +0.56 | +0.51 / +0.48 | both halves | 2e-05 | same gene group |
| [[CAP1]] | +0.56 | +0.60 / +0.44 | both halves | 3e-05 | STRING 419 |
| [[PCMT1]] | +0.56 | +0.51 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDA]] | -0.61 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[ZXDB]] | -0.61 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[RBM7]] | -0.61 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[ERAL1]] | -0.59 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[REPIN1]] | -0.59 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[ARFGAP2]] | -0.59 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[DXO]] | -0.59 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[UBAP2L]] | -0.58 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[HNRNPH2]] | -0.58 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[DTX3]] | -0.58 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[EIF2B5]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[MED12]] | -0.57 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.9, 7.5); signed map (-42.3, 8.3). **Vector** length 76.3, 27.6% of its response variance represented; |z| ≥ 3 in 697 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +0.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | -0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | -2.4 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +0.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -6.1 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -13.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -7.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | -3.5 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.7 | +1.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -2.1 | +0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 2/3 complex subunit 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,374,249-99,394,816 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARC41, p40-ARC, p41-ARC |
| Gene groups (HGNC) | Actin related protein 2/3 complex subunits; WD repeat domain containing |
| Reactome | 16 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; EPHB-mediated forward signaling; FCGR3A-mediated phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O15143](https://www.uniprot.org/uniprotkb/O15143) (Actin-related protein 2/3 complex subunit 1B):

> Component of the Arp2/3 complex, a multiprotein complex that mediates actin polymerization upon stimulation by nucleation-promoting factor (NPF). The Arp2/3 complex mediates the formation of branched actin networks in the cytoplasm, providing the force for cell motility. In addition to its role in the cytoplasmic cytoskeleton, the Arp2/3 complex also promotes actin polymerization in the nucleus, thereby regulating gene transcription and repair of damaged DNA. The Arp2/3 complex promotes …

**Summary**, from NCBI Gene [10095](https://www.ncbi.nlm.nih.gov/gene/10095):

> This gene encodes one of seven subunits of the human Arp2/3 protein complex. This subunit is a member of the SOP2 family of proteins and is most similar to the protein encoded by gene ARPC1A. The similarity between these two proteins suggests that they both may function as p41 subunit of the human Arp2/3 complex that has been implicated in the control of actin polymerization in cells. It is possible that the p41 subunit is involved in assembling and maintaining the structure of the Arp2/3 …

**Accessions** — [HGNC:704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:704) · Entrez [10095](https://www.ncbi.nlm.nih.gov/gene/10095) · UniProt [O15143](https://www.uniprot.org/uniprotkb/O15143) · Ensembl [ENSG00000130429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130429)

## Data

Gene col 5065: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5065); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5065, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5065]; `tensor/DDL_lfc|DDL_z.npy` [5065]; `embed/gene_vectors.npy` [5065]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5065 or target_col == 5065). Every well: [[ARPC1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARPC1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
