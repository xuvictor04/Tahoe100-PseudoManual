---
symbol: "NCSTN"
type: "gene"
col: 8574
ensembl_id: "ENSG00000162736"
name: "nicastrin"
location: "1q23.2"
module: 50
arm: "+"
pooled_cpm: 27.29
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# NCSTN

*nicastrin* — 1q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.66× (z +6.6, q 2e-08, up in 22 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.22× (z +3.8, q 0.015, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 3.35×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 3.41×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.513× (z -9.2, q 2e-17, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGT]] (+0.72, fdr 7e-06), [[EMC1]] (+0.71, fdr 7e-06), [[FKBP9]] (+0.70, fdr 7e-06); moves opposite to [[TMEM191A-1]] (-0.61, fdr 2e-04), [[EIF5B]] (-0.61, fdr 1e-05), [[CCDC112]] (-0.59, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8574.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 3.35×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 3.41×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +6.6 | 2e-08 | 22/33 (HEC-1-A, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.5 | 2e-08 | 30/44 (HEC-1-A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +6.2 | 8e-08 | 7/48 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +6.1 | 1e-07 | 25/38 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.015 | 22/48 (HS-578T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.19 | 10/47 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.26× | +3.0 | 0.19 | 16/47 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8574.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.513×** | -9.2 | 2e-17 | 44/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.528×** | -8.8 | 3e-16 | 40/48 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.543×** | -8.4 | 7e-15 | 40/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.666×** | -7.9 | 3e-13 | 32/47 (C32, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.587×** | -7.1 | 2e-10 | 36/47 (C32, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.588×** | -7.0 | 2e-10 | 34/47 (HS-578T, C32, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.606×** | -6.9 | 4e-10 | 42/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.649×** | -6.0 | 2e-07 | 30/47 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.651×** | -5.9 | 2e-07 | 34/46 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.630×** | -5.9 | 2e-07 | 34/48 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.691×** | -4.9 | 5e-05 | 29/45 (C-33 A, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.720×** | -4.0 | 0.002 | 24/48 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.580×** | -3.9 | 0.004 | 17/48 (HOP62, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -3.9 | 0.005 | 23/48 (CHP-212, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.740×** | -3.8 | 0.005 | 21/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.846× | -3.3 | 0.033 | 15/48 (SK-MEL-2, NCI-H460, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8574. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 18.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.35× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -8.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[CFPAC-1 (line)]] | alt | 29.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.357× (z -8.7) |
| [[A-172 (line)]] | wt | 49.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -8.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 33.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -11.8) ⚠ cell-cycle shift, explains ~45% of this change |
| [[C-33 A (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0827× (z -12.3) ⚠ toxic |
| [[C32 (line)]] | wt | 67.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -14.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[Hs 766T (line)]] | wt | 32.1 | 0 | 1 | — | [[Gemcitabine (drug)]] 5 µM 0.197× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0934× (z -8.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -9.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H661 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0895× (z -10.3) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -13.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8574), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGT]] | +0.72 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[EMC1]] | +0.71 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.70 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[RPN1]] | +0.69 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[CDK16]] | +0.69 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[CTSZ]] | +0.68 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[PEX19]] | +0.68 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[LAMP1]] | +0.67 | +0.57 / +0.71 | both halves | 9e-06 | STRING 747 |
| [[GANAB]] | +0.67 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[HCFC1]] | +0.67 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[MTX1]] | +0.67 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[SUMO3]] | +0.67 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM191A-1]] | -0.61 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[EIF5B]] | -0.61 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[CCDC112]] | -0.59 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[ATP5F1D]] ⚠ | -0.58 | -0.34 / -0.55 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL36]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[PPP1R35]] ⚠ | -0.57 | -0.39 / -0.56 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PDCD5]] | -0.57 | -0.38 / -0.62 | both halves | 6e-05 |  |
| [[COX5A]] ⚠ | -0.57 | -0.45 / -0.54 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CDKN2D]] | -0.57 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[SMIM26]] ⚠ | -0.56 | -0.36 / -0.58 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | -0.56 | -0.33 / -0.58 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.2, -22.6); signed map (-18.2, -33.2). **Vector** length 102, 24.6% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +2.4 |
|  | [[Folic acid (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.0 | +2.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.8 | -7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.8 | -6.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.5 | -5.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.4 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | nicastrin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.2 — chr1:160,343,294-160,358,952 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0253, APH2 |
| Gene groups (HGNC) | Gamma-secretase complex subunits |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING |
| Reactome | 37 pathways, smallest: Noncanonical activation of NOTCH3; NOTCH4 Activation and Transmission of Signal to the Nucleus; Regulated proteolysis of p75NTR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92542](https://www.uniprot.org/uniprotkb/Q92542) (Nicastrin):

> Essential subunit of the gamma-secretase complex, an endoprotease complex that catalyzes the intramembrane cleavage of integral membrane proteins such as Notch receptors and APP (amyloid-beta precursor protein). The gamma-secretase complex plays a role in Notch and Wnt signaling cascades and regulation of downstream processes via its role in processing key regulatory proteins, and by regulating cytosolic CTNNB1 levels.

**Summary**, from NCBI Gene [23385](https://www.ncbi.nlm.nih.gov/gene/23385):

> This gene encodes a type I transmembrane glycoprotein that is an integral component of the multimeric gamma-secretase complex. The encoded protein cleaves integral membrane proteins, including Notch receptors and beta-amyloid precursor protein, and may be a stabilizing cofactor required for gamma-secretase complex assembly. The cleavage of beta-amyloid precursor protein yields amyloid beta peptide, the main component of the neuritic plaque and the hallmark lesion in the brains of patients with …

**Accessions** — [HGNC:17091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17091) · Entrez [23385](https://www.ncbi.nlm.nih.gov/gene/23385) · UniProt [Q92542](https://www.uniprot.org/uniprotkb/Q92542) · Ensembl [ENSG00000162736](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162736)

## Data

Gene col 8574: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8574); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8574, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8574]; `tensor/DDL_lfc|DDL_z.npy` [8574]; `embed/gene_vectors.npy` [8574]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8574 or target_col == 8574). Every well: [[NCSTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCSTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
