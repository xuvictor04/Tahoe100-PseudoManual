---
symbol: "CNST"
type: "gene"
col: 8590
ensembl_id: "ENSG00000162852"
name: "consortin, connexin sorting protein"
location: "1q44"
module: 116
arm: "+"
pooled_cpm: 56.09
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# CNST

*consortin, connexin sorting protein* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.10× (z +13.6, q 1e-39, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.670× (z -7.1, q 6e-10, down in 25 of 41 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (RKO 0.0936×, NCI-H23 0.189×, C32 0.235×, A-427 0.281×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (Panc 03.27 0.129×, A-427 0.165×, SHP-77 0.288×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C32 0.387×, RKO 0.418×; ⚠ cell-cycle shift, explains ~82% of this change); [[Binimetinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.419×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CUTC]] (+0.60, fdr 1e-05), [[IL13RA2]] (+0.59, fdr 2e-05), [[BCL2A1]] (+0.59, fdr 1e-05); moves opposite to [[NCOA2]] (-0.44, fdr 4e-05), [[USP1]] (-0.42, fdr 8e-05), [[SMCHD1]] (-0.40, fdr 7e-05).
> It is in [[Module 116]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8590.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.10×** | +13.6 | 1e-39 | 46/48 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +9.6 | 1e-19 | 33/48 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +8.8 | 2e-16 | 38/48 (BT-474, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +7.0 | 5e-10 | 34/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +6.9 | 6e-10 | 29/48 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +6.8 | 7e-10 | 31/48 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +6.8 | 7e-10 | 33/47 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +6.5 | 7e-09 | 30/49 (MIA PaCa-2, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +6.4 | 9e-09 | 29/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +6.3 | 2e-08 | 26/47 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +6.1 | 4e-08 | 31/48 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +5.6 | 1e-06 | 26/49 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +5.1 | 1e-05 | 22/48 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 7e-05 | 23/48 (NCI-H23, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +4.5 | 2e-04 | 21/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 4e-04 | 24/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8590.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (RKO 0.0936×, NCI-H23 0.189×, C32 0.235×, A-427 0.281×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (Panc 03.27 0.129×, A-427 0.165×, SHP-77 0.288×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C32 0.387×, RKO 0.418×; ⚠ cell-cycle shift, explains ~82% of this change); [[Binimetinib (drug)]] 0.5 µM in 1 line (AsPC-1 0.419×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.670×** | -7.1 | 6e-10 | 25/41 (Panc 03.27, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.723×** | -6.0 | 6e-07 | 30/49 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.831× | -3.4 | 0.12 | 16/47 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.832× | -3.3 | 0.15 | 20/48 (HOP62, RKO, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.794× | -3.0 | 0.27 | 12/47 (SK-MEL-2, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8590. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 131 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +16.5) | — |
| [[C32 (line)]] | wt | 92.6 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -14.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 99.4 | 5 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.38× (z +10.2) | — |
| [[A-172 (line)]] | wt | 36.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +17.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +13.6) | — |
| [[PANC-1 (line)]] | alt | 64.1 | 2 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.42× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -10.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 105 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0936× (z -18.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 48.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -15.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 45.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.41× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 42.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.61× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 53.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.74× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 39.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -16.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 92.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.42× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -12.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 68.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.99× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 43.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +15.2) | — |
| [[AsPC-1 (line)]] | alt | 116 | 0 | 1 | — | [[Binimetinib (drug)]] 0.5 µM 0.419× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 61.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.77× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 42.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.49× (z +8.6) | — |
| [[J82 (line)]] | alt | 33.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 61.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 77.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -8.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 46.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.99× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 40.1 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0986× (z -13.4) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -10.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 79.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.395× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~15% of this change |
| [[SW480 (line)]] | alt | 45.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.11× (z +9.3) | — |
| [[A498 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 90.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8590), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUTC]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[IL13RA2]] | +0.59 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[BCL2A1]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[LNCOG]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[DSCAM]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[LINC01812]] | +0.55 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[CSGALNACT2]] | +0.55 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[NAV3]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[LAMA1]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ADTRP]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[KISS1]] | +0.54 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[MARCHF4]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOA2]] | -0.44 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[USP1]] | -0.42 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[SMCHD1]] | -0.40 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[RUSC1]] | -0.40 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[GMNN]] | -0.40 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[CNOT1]] | -0.40 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[DYRK1A]] | -0.40 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[CTPS2]] | -0.39 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[MFSD14A]] | -0.38 | -0.19 / -0.47 | ⚠ not reproduced | 8e-04 |  |
| [[DZIP1L]] | -0.38 | -0.33 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.0, 12.6); signed map (5.0, 53.8). **Vector** length 88.9, 21.5% of its response variance represented; |z| ≥ 3 in 1,278 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +13.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.4 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | +0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.3 | +5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.4 | +4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +3.9 |
| fall | [[venetoclax (drug)]] 5 µM |  | -3.1 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | consortin, connexin sorting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:246,566,444-246,668,595 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32001, PPP1R64; previously C1orf71 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PJW8](https://www.uniprot.org/uniprotkb/Q6PJW8) (Consortin):

> Required for targeting of connexins to the plasma membrane.

**Summary**, from NCBI Gene [163882](https://www.ncbi.nlm.nih.gov/gene/163882):

> Targeting of numerous transmembrane proteins to the cell surface is thought to depend on their recognition by cargo receptors that interact with the adaptor machinery for anterograde traffic at the distal end of the Golgi complex. Consortin (CNST) is an integral membrane protein that acts as a binding partner of connexins, the building blocks of gap junctions, and acts as a trans-Golgi network (TGN) receptor involved in connexin targeting to the plasma membrane and recycling from the cell …

**Accessions** — [HGNC:26486](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26486) · Entrez [163882](https://www.ncbi.nlm.nih.gov/gene/163882) · UniProt [Q6PJW8](https://www.uniprot.org/uniprotkb/Q6PJW8) · Ensembl [ENSG00000162852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162852)

## Data

Gene col 8590: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8590); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8590, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8590]; `tensor/DDL_lfc|DDL_z.npy` [8590]; `embed/gene_vectors.npy` [8590]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8590 or target_col == 8590). Every well: [[CNST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
