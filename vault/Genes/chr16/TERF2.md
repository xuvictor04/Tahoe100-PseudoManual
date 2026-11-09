---
symbol: "TERF2"
type: "gene"
col: 5346
ensembl_id: "ENSG00000132604"
name: "telomeric repeat binding factor 2"
location: "16q22.1"
module: 156
arm: "+"
pooled_cpm: 54.75
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# TERF2

*telomeric repeat binding factor 2* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.49× (z +10.7, q 5e-24, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.762× (z -7.3, q 2e-10, down in 27 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 0.833× (z -3.5, q 0.038, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A-172 0.188×, KATO III 0.234×, NCI-H460 0.359×, MIA PaCa-2 0.434×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.164×, SW480 0.522×, HS-578T 0.369×, RKO 0.434×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.164×, SW480 0.565×, NCI-H2030 0.451×; ⚠ toxic; transcription drop); [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (SW 1271 0.0947×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF41]] (+0.61, fdr 1e-05), [[RPP14]] (+0.61, fdr 1e-05), [[ZNF567]] (+0.59, fdr 7e-06); moves opposite to [[PDE5A]] (-0.52, fdr 5e-05), [[DSTN]] (-0.49, fdr 4e-05), [[CDKL2]] (-0.49, fdr 4e-05).
> It is in [[Module 156]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5346.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +10.7 | 5e-24 | 37/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +10.3 | 3e-22 | 28/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +9.2 | 8e-18 | 34/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +8.4 | 8e-15 | 33/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +8.3 | 8e-15 | 35/49 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +7.3 | 2e-11 | 29/47 (Hs 766T, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +7.3 | 2e-11 | 28/48 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +6.5 | 6e-09 | 27/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +6.0 | 1e-07 | 25/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change | **1.23×** | +5.5 | 2e-06 | 22/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.20×** | +5.0 | 3e-05 | 19/48 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.19× | +4.6 | 2e-04 | 17/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.18× | +4.6 | 2e-04 | 15/48 (Hs 766T, HCT15, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +4.5 | 3e-04 | 14/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.18× | +4.4 | 4e-04 | 11/48 (A549, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5346.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A-172 0.188×, KATO III 0.234×, NCI-H460 0.359×, MIA PaCa-2 0.434×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H23 0.164×, SW480 0.522×, HS-578T 0.369×, RKO 0.434×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.164×, SW480 0.565×, NCI-H2030 0.451×; ⚠ toxic; transcription drop); [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (SW 1271 0.0947×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.762×** | -7.3 | 2e-10 | 27/49 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.796×** | -5.9 | 1e-06 | 22/42 (A-172, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.818×** | -5.0 | 1e-04 | 22/45 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -4.5 | 8e-04 | 21/49 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.890× | -4.4 | 0.001 | 19/48 (RKO, NCI-H460, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.960× | -3.7 | 0.024 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.833×** | -3.5 | 0.038 | 15/47 (A-427, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.883× | -3.3 | 0.055 | 12/49 (MIA PaCa-2, C-33 A, …) | two highest doses |  |
| [[Radotinib (drug)]] 0.5 µM |  | 0.883× | -3.3 | 0.055 | 9/48 (SW 1271, LOX-IMVI, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.880× | -3.3 | 0.055 | 10/47 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.910× | -3.0 | 0.13 | 7/48 (SNU-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5346. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 116 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.522× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 53.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -19.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 78.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.98× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.434× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 74.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.451× (z -9.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 57.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -19.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 82.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.388× (z -8.6) ⚠ cell-cycle shift, explains ~1% of this change |
| [[HS-578T (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -9.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 51.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -20.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 49.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -13.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 44.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.0) | — |
| [[RKO (line)]] | wt | 74.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 61.1 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0947× (z -8.8) |
| [[A498 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 74.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5346), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF41]] | +0.61 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[RPP14]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ZNF567]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[GMEB1]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[METTL2A]] | +0.58 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[TFCP2]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[UMPS]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[TMEM168]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[OPA3]] | +0.58 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[SDHC]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[DDX19A]] | +0.57 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[MTG2]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE5A]] | -0.52 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[DSTN]] | -0.49 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[CDKL2]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[NPTN]] | -0.49 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[IFRD1]] | -0.48 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[IDH1]] | -0.48 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[VAMP1]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[RTN3]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.594). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.1, 3.5); signed map (-5.1, -16.2). **Vector** length 77.5, 14.3% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.3 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +4.4 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +2.8 | +9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | +2.6 | +4.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +0.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +1.5 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | telomeric repeat binding factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:69,355,567-69,408,571 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRF2; previously TRBF2 |
| Gene groups (HGNC) | Myb/SANT domain containing; Shelterin complex |
| Reactome | 28 pathways, smallest: Telomere C-strand synthesis initiation; Removal of the Flap Intermediate from the C-strand; Packaging Of Telomere Ends |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15554](https://www.uniprot.org/uniprotkb/Q15554) (Telomeric repeat-binding factor 2):

> Binds the telomeric double-stranded 5'-TTAGGG-3' repeat and plays a central role in telomere maintenance and protection against end-to-end fusion of chromosomes. In addition to its telomeric DNA-binding role, required to recruit a number of factors and enzymes required for telomere protection, including the shelterin complex, TERF2IP/RAP1 and DCLRE1B/Apollo. Component of the shelterin complex (telosome) that is involved in the regulation of telomere length and protection. Shelterin associates …

**Summary**, from NCBI Gene [7014](https://www.ncbi.nlm.nih.gov/gene/7014):

> This gene encodes a telomere specific protein, TERF2, which is a component of the telomere nucleoprotein complex. This protein is present at telomeres in metaphase of the cell cycle, is a second negative regulator of telomere length and plays a key role in the protective activity of telomeres. While having similar telomere binding activity and domain organization, TERF2 differs from TERF1 in that its N terminus is basic rather than acidic. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11729](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11729) · Entrez [7014](https://www.ncbi.nlm.nih.gov/gene/7014) · UniProt [Q15554](https://www.uniprot.org/uniprotkb/Q15554) · Ensembl [ENSG00000132604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132604)

## Data

Gene col 5346: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5346); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5346, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5346]; `tensor/DDL_lfc|DDL_z.npy` [5346]; `embed/gene_vectors.npy` [5346]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5346 or target_col == 5346). Every well: [[TERF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TERF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
