---
symbol: "NHLRC2"
type: "gene"
col: 12294
ensembl_id: "ENSG00000196865"
name: "NHL repeat containing 2"
location: "10q25.3"
module: 16
arm: "+"
pooled_cpm: 66.66
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# NHLRC2

*NHL repeat containing 2* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.55× (z +13.7, q 3e-40, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.528× (z -14.2, q 4e-43, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YEATS4]] (+0.72, fdr 7e-06), [[ZC3H7B]] (+0.71, fdr 7e-06), [[SENP1]] (+0.70, fdr 7e-06); moves opposite to [[MED26]] (-0.70, fdr 7e-06), [[DPM1]] (-0.69, fdr 7e-06), [[QPCTL]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KCNK6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12294.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +13.7 | 3e-40 | 37/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +10.7 | 4e-24 | 40/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +8.9 | 1e-16 | 30/44 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +8.0 | 1e-13 | 38/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +7.0 | 3e-10 | 33/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +6.7 | 2e-09 | 31/48 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +6.2 | 3e-08 | 25/49 (RKO, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +5.5 | 3e-06 | 25/48 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.074 | 17/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.086 | 17/47 (A-427, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.15× | +3.1 | 0.10 | 13/48 (NCI-H23, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.10 | 20/47 (KATO III, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12294.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.528×** | -14.2 | 4e-43 | 46/48 (SW480, C-33 A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.673×** | -8.3 | 2e-14 | 36/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.781×** | -7.8 | 1e-12 | 31/49 (RKO, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.731×** | -7.0 | 4e-10 | 31/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.553×** | -6.9 | 6e-10 | 31/43 (PANC-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.744×** | -6.6 | 4e-09 | 30/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.752×** | -6.4 | 2e-08 | 27/48 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.782×** | -5.5 | 3e-06 | 26/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.732×** | -5.0 | 4e-05 | 26/49 (PANC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.816×** | -4.5 | 3e-04 | 20/48 (C-33 A, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.698×** | -4.2 | 0.001 | 20/48 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.703×** | -4.1 | 0.002 | 21/48 (LOX-IMVI, RKO, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.719×** | -3.8 | 0.005 | 25/48 (CFPAC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.836× | -3.8 | 0.005 | 21/48 (HS-578T, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 0.5 µM |  | 0.844× | -3.8 | 0.006 | 15/48 (HEC-1-A, J82, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.850× | -3.4 | 0.021 | 19/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12294. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 113 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +18.0) | [[Bortezomib (drug)]] 0.05 µM 0.540× (z -8.8) |
| [[A-172 (line)]] | wt | 64.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +16.8) | — |
| [[C-33 A (line)]] | alt | 96.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0984× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.262× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.449× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 48.9 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.344× (z -10.0) |
| [[SW480 (line)]] | alt | 78.1 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.322× (z -16.8) |
| [[A-427 (line)]] | wt | 70.5 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.328× (z -13.4) |
| [[A498 (line)]] | wt | 63.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.7) | — |
| [[LoVo (line)]] | wt | 72.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.95× (z +8.6) ⚠ toxic; transcription drop | [[Auranofin (drug)]] 5 µM 0.475× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 55.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.9) | [[Auranofin (drug)]] 5 µM 0.414× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 92.0 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.389× (z -13.6) |
| [[A549 (line)]] | wt | 71.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 42.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.403× (z -9.7) |
| [[HT-29 (line)]] | alt | 55.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 68.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 50.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 67.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.369× (z -11.1) |
| [[RKO (line)]] | wt | 66.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -11.8) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SHP-77 (line)]] | alt | 90.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.445× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 63.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.304× (z -12.7) |
| [[SNU-1 (line)]] | wt | 76.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -13.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 92.1 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.104× (z -10.1) |
| [[SW48 (line)]] | wt | 47.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.289× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 109 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12294), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YEATS4]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[ZC3H7B]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[SENP1]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[PTAR1]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[VEZF1]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[YTHDC2]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[HYLS1]] | +0.67 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[GCFC2]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[POGLUT1]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[MYEF2]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[MIOS]] | +0.65 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[DIS3L]] | +0.65 | +0.65 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED26]] | -0.70 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[DPM1]] | -0.69 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[QPCTL]] | -0.68 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[DEDD2]] | -0.65 | -0.57 / -0.64 | both halves | 9e-06 |  |
| [[DHDDS]] | -0.65 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[RABGEF1]] | -0.64 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[MACO1]] | -0.64 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ABHD17B]] | -0.63 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.63 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[NDEL1]] | -0.63 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[POR]] | -0.61 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[MRPL55]] | -0.61 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK6]] | B | KCNK6 activity lowers NHLRC2's level | lines that do not express KCNK6 (12) vs lines expressing it (38) | 1.30× higher at baseline in the lines without KCNK6 | 0.060 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.570). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-16.8, -6.4); signed map (15.0, -30.5). **Vector** length 125, 33.7% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +10.7 | +10.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.2 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +13.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +3.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.9 | -14.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.6 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.5 | -6.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.0 | -6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -4.3 | -7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.2 | -5.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.5 | -4.1 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -2.7 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | NHL repeat containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:113,854,661-113,917,194 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25621, FLJ20147, FLJ33312, MGC45492, DKFZp779F115 |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBF2](https://www.uniprot.org/uniprotkb/Q8NBF2) (NHL repeat-containing protein 2):

> Required for normal embryonic development.

**Summary**, from NCBI Gene [374354](https://www.ncbi.nlm.nih.gov/gene/374354):

> Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24731](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24731) · Entrez [374354](https://www.ncbi.nlm.nih.gov/gene/374354) · UniProt [Q8NBF2](https://www.uniprot.org/uniprotkb/Q8NBF2) · Ensembl [ENSG00000196865](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196865)

## Data

Gene col 12294: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12294); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12294, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12294]; `tensor/DDL_lfc|DDL_z.npy` [12294]; `embed/gene_vectors.npy` [12294]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12294 or target_col == 12294). Every well: [[NHLRC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NHLRC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
